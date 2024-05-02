CREATE TABLE transactions (
    id SERIAL NOT NULL,
    "timestamp" timestamp without time zone,
    price numeric,
    user_id integer,
    row_hash character varying(64)
);

CREATE TABLE statistics (
    id SERIAL NOT NULL,
    total_rows integer,
    average_price double precision,
    min_price double precision,
    max_price double precision,
    last_updated timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);