from prefect import task, flow
import pandas as pd
from sqlalchemy import Integer, Float, SmallInteger, String, DateTime, DATE, TIME, DECIMAL
import datetime as dt


@task
def load_data(engine, schema):
    table_names = ["aankomst", "banen", "klant", "luchthavens", "maatschappijen", "planning", "vertrek", "vliegtuig", "vliegtuigtype", "vlucht", "weer"]
    dataframes = {}
    for table in table_names:
        dataframes[table] = pd.read_sql_table(table_name=table, con=engine, schema=schema)
    return dataframes

@task
# Validation and conversion functions for each table
def validate_and_convert(df, schema, illegal_chars):
    def contains_illegal_chars(value, illegal_chars):
        if any(char in str(value) for char in illegal_chars):
            return True
        return False
    
    validated_rows = []
    archived_rows = []
    for index, row in df.iterrows():
        try:
            converted_row = {}
            for column, column_info in schema.items():
                if pd.isna(row[column]):
                    if column_info.nullable:
                        converted_row[column] = None
                    else:
                        raise ValueError(f"Null value in non-nullable column: {column}")
                elif '\\N' in str(row[column]):
                    converted_row[column] = None
                else:
                    if column in illegal_chars and contains_illegal_chars(row[column], illegal_chars[column]):
                        raise ValueError(f"Illegal character found in column: {column}")
                    
                    
                    value = row[column]
                    
                    if isinstance(column_info.type, Integer):
                        converted_row[column] = int(value)
                    elif isinstance(column_info.type, Float):
                        converted_row[column] = float(value)
                    elif isinstance(column_info.type, SmallInteger):
                        converted_row[column] = int(value)
                    elif isinstance(column_info.type, String):
                        if len(str(value)) > column_info.type.length:
                            raise ValueError(f"String value too long for column: {column}")
                        converted_row[column] = str(value)
                    elif isinstance(column_info.type, DateTime):
                        converted_row[column] = pd.to_datetime(value)
                    elif isinstance(column_info.type, DATE):
                        converted_row[column] = pd.to_datetime(value).date()
                    elif isinstance(column_info.type, TIME):
                        converted_row[column] = dt.strptime(value, '%I:%M %p').time()
                    elif isinstance(column_info.type, DECIMAL):
                        converted_row[column] = round(float(value), column_info.type.scale)
            validated_rows.append(converted_row)
        except (ValueError, TypeError, AttributeError) as e:
            archived_rows.append(row.to_dict())
    return pd.DataFrame(validated_rows), pd.DataFrame(archived_rows)


@flow
def clean_and_insert_data(engine, schema_raw, schema_cleansed, schema_archived, illegal_chars):
    raw_data = load_data(engine, schema_raw)

    cleansed_data = {}
    archived_data = {}

    for table, df in raw_data.items():
        print(f"Processing {table}")
        cleansed_data[table], archived_data[table] = validate_and_convert(df, schema_cleansed[table], illegal_chars)

    def get_sqlalchemy_dtypes(schema):
        return {column_name: column_info.type for column_name, column_info in schema.items()}

    def insert_data(data, schema, engine, schemas):
        for table, df in data.items():
            print(f'Inserting data into {schema}.{table}')
            if not df.empty:
                dtypes = get_sqlalchemy_dtypes(schemas[table])
                df.to_sql(name=table, con=engine, schema=schema, if_exists='replace', index=False, dtype=dtypes)

    insert_data(cleansed_data, 'cleansed', engine, schema_cleansed)
    insert_data(archived_data, 'archived', engine, schema_archived)
    

