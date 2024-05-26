from sqlalchemy import Column, Integer, String, CHAR, SmallInteger, DateTime, Float, DECIMAL, TIME, DATE

schema_cleansed = {
    "aankomst": {
        "Vluchtid": Column(Integer),
        "Vliegtuigcode": Column(String(8)),
        "Terminal": Column(CHAR(1)),
        "Gate": Column(String(2)),
        "Baan": Column(CHAR(1)),
        "Bezetting": Column(SmallInteger),
        "Vracht": Column(CHAR(2)),
        "Aankomsttijd": Column(DateTime)
    },
    "banen": {
        "Baannummer": Column(CHAR(1), nullable=False),
        "Code": Column(String(7)),
        "Naam": Column(String(30)),
        "Lengte": Column(SmallInteger)
    },
    "klant": {
        "Vluchtid": Column(Integer, nullable=False),
        "Operatie": Column(DECIMAL(2, 1)),
        "Faciliteiten": Column(DECIMAL(2, 1)),
        "Shops": Column(DECIMAL(2, 1))
    },
    "luchthavens": {
        "Airport": Column(String(100)),
        "City": Column(String(100)),
        "Country": Column(String(100)),
        "IATA": Column(CHAR(3), nullable=False),
        "ICAO": Column(CHAR(4)),
        "Lat": Column(Float),
        "Lon": Column(Float),
        "Alt": Column(SmallInteger),
        "TZ": Column(DECIMAL(3, 1)),
        "DST": Column(CHAR(1)),
        "Tz": Column(String(100))
    },
    "maatschappijen": {
        "Name": Column(String(50)),
        "IATA": Column(String(3), nullable=False),
        "ICAO": Column(String(3))
    },
    "planning": {
        "Vluchtnr": Column(String(7)),
        "Airlinecode": Column(String(3)),
        "Destcode": Column(CHAR(3)),
        "Planterminal": Column(CHAR(1)),
        "Plangate": Column(String(2)),
        "Plantijd": Column(TIME)
    },
    "vertrek": {
        "Vluchtid": Column(Integer, nullable=False),
        "Vliegtuigcode": Column(String(8)),
        "Terminal": Column(CHAR(1)),
        "Gate": Column(String(2)),
        "Baan": Column(CHAR(1)),
        "Bezetting": Column(SmallInteger),
        "Vracht": Column(CHAR(2)),
        "Vertrektijd": Column(DateTime, nullable=False)
    },
    "vliegtuig": {
        "Airlinecode": Column(String(3)),
        "Vliegtuigcode": Column(String(8), nullable=False),
        "Vliegtuigtype": Column(CHAR(3)),
        "Bouwjaar": Column(Integer)
    },
    "vliegtuigtype": {
        "IATA": Column(CHAR(3), nullable=False),
        "ICAO": Column(String(4)),
        "Merk": Column(String(50)),
        "Type": Column(String(100)),
        "Wake": Column(String(3)),
        "Cat": Column(String(10)),
        "Capaciteit": Column(String(3)),
        "Vracht": Column(String(2))
    },
    "vlucht": {
        "Vluchtid": Column(Integer, nullable=False),
        "Vluchtnr": Column(String(7), nullable=False),
        "Airlinecode": Column(String(3)),
        "Destcode": Column(CHAR(3)),
        "Vliegtuigcode": Column(String(8)),
        "Datum": Column(DATE)
    },
    "weer": {
        "Datum": Column(DATE, nullable=False),
        "DDVEC": Column(SmallInteger),
        "FHVEC": Column(SmallInteger),
        "FG": Column(SmallInteger),
        "FHX": Column(SmallInteger),
        "FHXH": Column(SmallInteger),
        "FHN": Column(SmallInteger),
        "FHNH": Column(SmallInteger),
        "FXX": Column(SmallInteger),
        "FXXH": Column(SmallInteger),
        "TG": Column(SmallInteger),
        "TN": Column(SmallInteger),
        "TNH": Column(SmallInteger),
        "TX": Column(SmallInteger),
        "TXH": Column(SmallInteger),
        "T10N": Column(SmallInteger),
        "T10NH": Column(SmallInteger),
        "SQ": Column(SmallInteger),
        "SP": Column(SmallInteger),
        "Q": Column(SmallInteger),
        "DR": Column(SmallInteger),
        "RH": Column(SmallInteger),
        "RHX": Column(SmallInteger),
        "RHXH": Column(SmallInteger),
        "PG": Column(SmallInteger),
        "PX": Column(SmallInteger),
        "PXH": Column(SmallInteger),
        "PN": Column(SmallInteger),
        "PNH": Column(SmallInteger),
        "VVN": Column(SmallInteger),
        "VVNH": Column(SmallInteger),
        "VVX": Column(SmallInteger),
        "VVXH": Column(SmallInteger),
        "NG": Column(SmallInteger),
        "UG": Column(SmallInteger),
        "UX": Column(SmallInteger),
        "UXH": Column(SmallInteger),
        "UN": Column(SmallInteger),
        "UNH": Column(SmallInteger),
        "EV2": Column(SmallInteger)
    }
}

illegal_chars = {
    "IATA": ['-', ' ', ';', '^', '+', '\\']
}