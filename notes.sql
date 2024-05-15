CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT
);

INSERT INTO notes (title, content) VALUES ('Note 1', 'Content of Note 1');
INSERT INTO notes (title, content) VALUES ('Note 2', 'Content of Note 2');
INSERT INTO notes (title, content) VALUES ('Note 3', 'Content of Note 3');

DROP TABLE notes;