--Create users with unique column 

--Create a users Table 
CREATE TABLE IF NOT EXISTS user (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
)
