CREATE USER eruser;
CREATE DATABASE fire
  WITH OWNER = postgres
    TEMPLATE = 'template_postgis'
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    CONNECTION LIMIT = -1;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO eruser;
fire < /code/postgres/data/fire_db_2010
