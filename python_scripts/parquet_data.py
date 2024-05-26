from prefect import task, flow
import pandas as pd
import os

@task
def load_data(engine, schema):
    table_names = ["aankomst", "banen", "klant", "luchthavens", "maatschappijen", "planning", "vertrek", "vliegtuig", "vliegtuigtype", "vlucht", "weer"]
    dataframes = {}
    for table in table_names:
        dataframes[table] = pd.read_sql_table(table_name=table, con=engine, schema=schema)
    return dataframes

@task 
def join_fact_dataframes(df_vlucht, df_vertrek, df_planning):
    def time_to_minutes(t):
        return t.hour * 60 + t.minute + t.second / 60

    merged_df = pd.merge(df_vlucht, df_vertrek, on=['Vluchtid', 'Vliegtuigcode'])
    merged_df['Vertrektijd'] = merged_df['Vertrektijd'].dt.time
    final_df = pd.merge(merged_df, df_planning, on=['Vluchtnr', 'Airlinecode', 'Destcode'])
    final_df['Vertraging'] = final_df['Vertrektijd'].apply(time_to_minutes) - final_df['Plantijd'].apply(time_to_minutes)
    final_df.sort_values(by='Vluchtid', ascending=True, inplace=True)
    return final_df

@task
def join_vlucht_dataframes(df_vliegtuig, df_vliegtuigtype):
    dim_vliegtuig = pd.merge(df_vliegtuig, df_vliegtuigtype, left_on='Vliegtuigtype', right_on='IATA')
    return dim_vliegtuig

@task
def write_to_parquet(df, file_path):

    directory = "parquet_data"

    if not os.path.exists(directory):
        os.makedirs(directory)
    df.to_parquet(file_path, engine='pyarrow')

@flow
def join_dataframes_to_parquet(engine):
    cleansed_data = load_data(engine, 'cleansed')
    df_vlucht = cleansed_data['vlucht']
    df_vertrek = cleansed_data['vertrek']
    df_planning = cleansed_data['planning']

    fact = join_fact_dataframes(df_vlucht, df_vertrek, df_planning)

    df_vliegtuig = cleansed_data['vliegtuig']
    df_vliegtuigtype = cleansed_data['vliegtuigtype']

    dim_vliegtuig = join_vlucht_dataframes(df_vliegtuig, df_vliegtuigtype)

    dim_banen = cleansed_data['banen']
    dim_klant = cleansed_data['klant']
    dim_luchthavens = cleansed_data['luchthavens'].rename(columns={'IATA': 'Destcode'})
    dim_maatschappijen = cleansed_data['maatschappijen'].rename(columns={'IATA': 'Airlinecode'})
    dim_weer = cleansed_data['weer']

    write_to_parquet(fact, 'parquet_data/fact.parquet')
    write_to_parquet(dim_vliegtuig, 'parquet_data/dim_vliegtuig.parquet')
    write_to_parquet(dim_banen, 'parquet_data/dim_banen.parquet')
    write_to_parquet(dim_klant, 'parquet_data/dim_klant.parquet')
    write_to_parquet(dim_luchthavens, 'parquet_data/dim_luchthavens.parquet')
    write_to_parquet(dim_maatschappijen, 'parquet_data/dim_maatschappijen.parquet')
    write_to_parquet(dim_weer, 'parquet_data/dim_weer.parquet')