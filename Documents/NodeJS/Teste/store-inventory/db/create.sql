CREATE SCHEMA store;

CREATE TABLE IF NOT EXISTS store.clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL,
    price INTEGER NOT NULL,

)