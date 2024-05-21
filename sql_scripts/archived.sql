-- Schema aanmaken indien het nog niet bestaat
CREATE SCHEMA IF NOT EXISTS archived;

-- Tabellen verwijderen indien ze bestaan
DROP TABLE IF EXISTS archived.aankomst, archived.banen, archived.klant, archived.luchthavens, archived.maatschappijen, archived.planning, archived.vertrek, archived.vliegtuig, archived.vliegtuigtype, archived.vlucht, archived.weer CASCADE;