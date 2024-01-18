-- Create  a users table with enum 

-- users table 
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') DEFAULT 1
)
