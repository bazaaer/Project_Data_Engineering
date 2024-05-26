from prefect import flow
from python_scripts.prep_database import prep_database
from python_scripts.load_data import load_and_insert
from python_scripts.clean_data import clean_and_insert_data
from python_scripts.parquet_data import join_dataframes_to_parquet

from sql_scripts.schema_cleansed import schema_cleansed, illegal_chars
from sql_scripts.schema_archived import schema_archived

from sqlalchemy import create_engine

host='db'
dbname='postgres'
user='postgres'
password='postgres'
port=5432

engine = create_engine('postgresql://postgres:postgres@db:5432/postgres')

@flow
def main():
    prep_database(host, dbname, user, password, port)
    load_and_insert(engine, 'raw')
    clean_and_insert_data(engine, 'raw', schema_cleansed, schema_archived, illegal_chars)
    join_dataframes_to_parquet(engine)

if __name__ == '__main__':
    main()

