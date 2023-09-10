--creating database--
CREATE DATABASE flat_organization_hierarchy;

--Switch to the newly created database--
USE flat_organization_hierarchy;

--Create the 'employee' table--
CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    supervisor_id INT,
    position ENUM('left', 'right')
);

-- Insert data into the employee table to represent organizational hierarchy--
INSERT INTO employee (name, supervisor_id, position)
VALUES
    ('A', NULL, NULL),
    ('B', 1, 'left'),
    ('C', 1, 'right'),
    ('D', 2, 'left'),
    ('G', 3, 'right'),
    ('E', 4, 'left'),
    ('F', 4, 'right'),
    ('H', 5, 'left'),
    ('I', 5, 'right');

--verify that the database and tables have been created correctly--
-- Select all employees
SELECT * FROM employee;

-- Describe the 'employee' table
DESCRIBE employee;
