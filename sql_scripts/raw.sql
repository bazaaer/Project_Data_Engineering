-- Schema aanmaken indien het nog niet bestaat
CREATE SCHEMA IF NOT EXISTS raw;

-- Tabellen verwijderen indien ze bestaan
DROP TABLE IF EXISTS raw.aankomst, raw.banen, raw.klant, raw.luchthavens, raw.maatschappijen, raw.planning, raw.vertrek, raw.vliegtuig, raw.vliegtuigtype, raw.vlucht, raw.weer CASCADE;