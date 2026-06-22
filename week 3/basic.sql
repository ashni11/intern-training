CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

INSERT INTO users(name, email)
VALUES
('Ashni', 'ashni@gmail.com'),
('Priya', 'priya@gmail.com'),
('Rahul', 'rahul@gmail.com'),
('Anu', 'anu@gmail.com'),
('Karthik', 'karthik@gmail.com');

SELECT * FROM users;

SELECT * FROM users
WHERE id > 2;

SELECT * FROM users
WHERE name LIKE 'A%';

SELECT * FROM users
ORDER BY name;

SELECT * FROM users
ORDER BY email;
