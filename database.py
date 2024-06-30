CREATE DATABASE project_1;

USE project_1;

CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    votes INT DEFAULT 0
);

INSERT INTO candidates (name, votes) VALUES
('Candidate A', 0),
('Candidate B', 0),
('Candidate C', 0);

