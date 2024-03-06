-- Create users table
CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(128) UNIQUE NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    sex VARCHAR(36) NOT NULL,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL
);

-- Create bmi_records table
CREATE TABLE bmi_records (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    height INT NOT NULL,
    weight INT NOT NULL,
    bmi INT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);