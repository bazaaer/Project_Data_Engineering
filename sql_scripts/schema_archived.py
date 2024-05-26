from sqlalchemy import Column, String

schema_archived = {
    "aankomst": {
        "Vluchtid": Column(String),
        "Vliegtuigcode": Column(String),
        "Terminal": Column(String),
        "Gate": Column(String),
        "Baan": Column(String),
        "Bezetting": Column(String),
        "Vracht": Column(String),
        "Aankomsttijd": Column(String)
    },
    "banen": {
        "Baannummer": Column(String),
        "Code": Column(String),
        "Naam": Column(String),
        "Lengte": Column(String)
    },
    "klant": {
        "Vluchtid": Column(String),
        "Operatie": Column(String),
        "Faciliteiten": Column(String),
        "Shops": Column(String)
    },
    "luchthavens": {
        "Airport": Column(String),
        "City": Column(String),
        "Country": Column(String),
        "IATA": Column(String),
        "ICAO": Column(String),
        "Lat": Column(String),
        "Lon": Column(String),
        "Alt": Column(String),
        "TZ": Column(String),
        "DST": Column(String),
        "Tz": Column(String)
    },
    "maatschappijen": {
        "Name": Column(String),
        "IATA": Column(String),
        "ICAO": Column(String)
    },
    "planning": {
        "Vluchtnr": Column(String),
        "Airlinecode": Column(String),
        "Destcode": Column(String),
        "Planterminal": Column(String),
        "Plangate": Column(String),
        "Plantijd": Column(String)
    },
    "vertrek": {
        "Vluchtid": Column(String),
        "Vliegtuigcode": Column(String),
        "Terminal": Column(String),
        "Gate": Column(String),
        "Baan": Column(String),
        "Bezetting": Column(String),
        "Vracht": Column(String),
        "Vertrektijd": Column(String)
    },
    "vliegtuig": {
        "Airlinecode": Column(String),
        "Vliegtuigcode": Column(String),
        "Vliegtuigtype": Column(String),
        "Bouwjaar": Column(String)
    },
    "vliegtuigtype": {
        "IATA": Column(String),
        "ICAO": Column(String),
        "Merk": Column(String),
        "Type": Column(String),
        "Wake": Column(String),
        "Cat": Column(String),
        "Capaciteit": Column(String),
        "Vracht": Column(String)
    },
    "vlucht": {
        "Vluchtid": Column(String),
        "Vluchtnr": Column(String),
        "Airlinecode": Column(String),
        "Destcode": Column(String),
        "Vliegtuigcode": Column(String),
        "Datum": Column(String)
    },
    "weer": {
        "Datum": Column(String),
        "DDVEC": Column(String),
        "FHVEC": Column(String),
        "FG": Column(String),
        "FHX": Column(String),
        "FHXH": Column(String),
        "FHN": Column(String),
        "FHNH": Column(String),
        "FXX": Column(String),
        "FXXH": Column(String),
        "TG": Column(String),
        "TN": Column(String),
        "TNH": Column(String),
        "TX": Column(String),
        "TXH": Column(String),
        "T10N": Column(String),
        "T10NH": Column(String),
        "SQ": Column(String),
        "SP": Column(String),
        "Q": Column(String),
        "DR": Column(String),
        "RH": Column(String),
        "RHX": Column(String),
        "RHXH": Column(String),
        "PG": Column(String),
        "PX": Column(String),
        "PXH": Column(String),
        "PN": Column(String),
        "PNH": Column(String),
        "VVN": Column(String),
        "VVNH": Column(String),
        "VVX": Column(String),
        "VVXH": Column(String),
        "NG": Column(String),
        "UG": Column(String),
        "UX": Column(String),
        "UXH": Column(String),
        "UN": Column(String),
        "UNH": Column(String),
        "EV2": Column(String)
    }
}
