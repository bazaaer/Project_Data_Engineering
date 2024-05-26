from prefect import task, flow

import psycopg2

@task
def make_connection(host, dbname, user, password, port):
    conn = psycopg2.connect(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )
    
    return conn

@task
def fetch_scripts(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()

    return sql_script

@flow
def prep_database(host, dbname, user, password, port):
    conn = make_connection(
        host=host,
        dbname=dbname,
        user=user,
        password=password,
        port=port
    )

    raw = fetch_scripts('./sql_scripts/raw.sql')
    cleansed = fetch_scripts('./sql_scripts/cleansed.sql')
    archived = fetch_scripts('./sql_scripts/archived.sql')

    cur = conn.cursor()

    cur.execute(raw)
    cur.execute(cleansed)
    cur.execute(archived)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    prep_database()