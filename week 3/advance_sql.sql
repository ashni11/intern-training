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

CREATE TABLE posts(
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    content TEXT,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO posts(title, content, user_id)
VALUES
('SQL Basics', 'Learning SQL', 1),
('FastAPI CRUD', 'Building APIs', 1),
('Python OOP', 'Classes and Objects', 2),
('PostgreSQL', 'Database Concepts', 3),
('maths','integration',4);

SELECT * FROM posts;

UPDATE posts
SET title = 'Advanced SQL'
WHERE id = 1;
SELECT * FROM posts;

DELETE FROM posts
WHERE id=3;
SELECT * FROM posts;


select name,title
from users
inner join posts
on users.id = posts.id


select *
from users 
left join posts
on users.id=posts.id;

select name,count(*)
from users 
inner join posts
on users.id=posts.id
GROUP BY name;













