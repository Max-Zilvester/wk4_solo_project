DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    gender VARCHAR(255)
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(255),
    status VARCHAR(255),
    member_id INT REFERENCES members(id)
);
