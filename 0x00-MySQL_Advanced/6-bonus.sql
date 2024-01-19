-- stored procedure 

-- make correctons
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
LANGUAGE SQL
COMMENT 'update a user project corrections'
DETERMINISTIC 
CONTAINS SQL
SQL SECURITY DEFINER
BEGIN
  DECLARE uproject_name VARCHAR(255);
  DECLARE uproject_id INT;

  SELECT
  name INTO uproject_name 
  FROM projects 
  WHERE name = project_name; 

  IF uproject_name IS NULL
    THEN
    INSERT INTO projects (name) VALUES (project_name);
  END IF; 

  SELECT id INTO uproject_id 
  FROM project 
  WHERE name = project_name LIMIT 1;

  INSERT INTO corrections
  (user_id, project_id, score) 
  values
  (user_id, uproject_id, score);
END$$
