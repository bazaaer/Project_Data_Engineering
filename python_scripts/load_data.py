from prefect import flow

from sqlalchemy import String
from datetime import datetime as dt


import pandas as pd

@flow
def load_and_insert(engine, SCHEMA='raw'):
    TABEL = 'aankomst'
    df = pd.read_csv(f'./source_data/export_{TABEL}.txt', sep='\t', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Vluchtid": String,
        "Vliegtuigcode": String,
        "Terminal": String,
        "Gate": String,
        "Baan": String,
        "Bezetting": String,
        "Vracht": String,
        "Aankomsttijd": String,
    })

    TABEL = 'banen'
    file_path = f'./source_data/export_{TABEL}.csv' 
    df = pd.read_csv(file_path, sep=';', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Baannummer": String,
        "Code": String,
        "Naam": String,
        "Lengte": String
    })

    TABEL = 'klant'
    file_path = f'./source_data/export_{TABEL}.csv'
    df = pd.read_csv(file_path, sep=';', dtype=str)
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Vluchtid": String,
        "Operatie": String,
        "Faciliteiten": String,
        "Shops": String
    })

    TABEL = 'luchthavens'
    file_path = f'./source_data/export_{TABEL}.txt'
    df = pd.read_csv(file_path, sep='\t', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Airport": String,
        "City": String,
        "Country": String,
        "IATA": String,
        "ICAO": String,
        "Lat": String,
        "Lon": String,
        "Alt": String,
        "TZ": String,
        "DST": String,
        "Tz": String
    })


    TABEL = 'maatschappijen'
    file_path = f'./source_data/export_{TABEL}.txt'
    df = pd.read_csv(file_path, sep='\t', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Name": String,
        "IATA": String,
        "ICAO": String
    })

    TABEL = 'planning'
    file_path = f'./source_data/export_{TABEL}.txt'
    df = pd.read_csv(file_path, sep='\t', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Vluchtnr": String,
        "Airlinecode": String,
        "Destcode": String,
        "Planterminal": String,
        "Plangate": String,
        "Plantijd": String
    })

    TABEL = 'vertrek'
    file_path = f'./source_data/export_{TABEL}.txt'
    df = pd.read_csv(file_path, sep='\t', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Vluchtid": String,
        "Vliegtuigcode": String,
        "Terminal": String,
        "Gate": String,
        "Baan": String,
        "Bezetting": String,
        "Vracht": String,
        "Vertrektijd": String
    })

    TABEL = 'vliegtuig'
    file_path = f'./source_data/export_{TABEL}.txt'
    df = pd.read_csv(file_path, sep='\t', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Vluchtid": String,
        "Vliegtuigcode": String,
        "Terminal": String,
        "Gate": String,
        "Baan": String,
        "Bezetting": String,
        "Vracht": String,
        "Vertrektijd": String
    })

    TABEL = 'vliegtuigtype'
    file_path = f'./source_data/export_{TABEL}.csv'
    df = pd.read_csv(file_path, sep=';', dtype=str)
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "IATA": String,
        "ICAO": String,
        "Merk": String,
        "Type": String,
        "Wake": String,
        "Cat": String,
        "Capaciteit": String,
        "Vracht": String
    })

    TABEL = 'vlucht'
    file_path = f'./source_data/export_{TABEL}.txt'
    df = pd.read_csv(file_path, sep='\t', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Vluchtid": String,
        "Vluchtnr": String,
        "Airlinecode": String,
        "Destcode": String,
        "Vliegtuigcode": String,
        "Datum": String
    })

    TABEL = 'weer'
    file_path = f'./source_data/export_{TABEL}.txt'
    df = pd.read_csv(file_path, sep='\t', dtype=str, encoding='raw_unicode_escape')
    df.to_sql(TABEL, con=engine, schema=SCHEMA, if_exists='replace', index=False, dtype={
        "Datum": String,
        "DDVEC": String,
        "FHVEC": String,
        "FG": String,
        "FHX": String,
        "FHXH": String,
        "FHN": String,
        "FHNH": String,
        "FXX": String,
        "FXXH": String,
        "TG": String,
        "TN": String,
        "TNH": String,
        "TX": String,
        "TXH": String,
        "T10N": String,
        "T10NH": String,
        "SQ": String,
        "SP": String,
        "Q": String,
        "DR": String,
        "RH": String,
        "RHX": String,
        "RHXH": String,
        "PG": String,
        "PX": String,
        "PXH": String,
        "PN": String,
        "PNH": String,
        "VVN": String,
        "VVNH": String,
        "VVX": String,
        "VVXH": String,
        "NG": String,
        "UG": String,
        "UX": String,
        "UXH": String,
        "UN": String,
        "UNH": String,
        "EV2": String
    })

if __name__ == '__main__':
    load_and_insert()