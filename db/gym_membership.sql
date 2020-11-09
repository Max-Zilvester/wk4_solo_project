DROP TABLE gyms;
DROP TABLE events;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255)
);

CREATE TABLE gyms (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    event_id INT REFERENCES events(id) ON DELETE CASCADE,
    availability VARCHAR(255)
);