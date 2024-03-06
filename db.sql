-- prepares a dev MySQL server for the project.
CREATE DATABASE IF NOT EXISTS bmi_db;
CREATE USER IF NOT EXISTS 'm'@'localhost' IDENTIFIED BY 'm';
GRANT ALL PRIVILEGES ON bmi_db.* TO 'm'@'localhost';
GRANT SELECT ON performance_schema.* TO 'm'@'localhost';
FLUSH PRIVILEGES;
