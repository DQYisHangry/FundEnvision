-- db/init.sql
DROP DATABASE IF EXISTS funds_db;
CREATE DATABASE funds_db;
USE funds_db;

CREATE TABLE etf_nav (
    ticker VARCHAR(10),
    fund_name VARCHAR(255),
    nav_date DATE,
    nav DECIMAL(10, 2),
    PRIMARY KEY (ticker, nav_date)
);
