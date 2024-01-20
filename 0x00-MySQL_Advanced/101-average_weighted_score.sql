-- COMPUTE WEIGHTED AVERAGR

-- Stored procedure
DELIMITER $$ 
CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
LANGUAGE SQL
COMMENT 'Calculate average weighted score for a user'
NOT DETERMINISTIC
SQL SECURITY DEFINER
CONTAINS SQL
BEGIN
  DECLARE uweight INT;
  DECLARE weightSum INT;
  DECLARE i INT DEFAULT 0; 
  DECLARE len INT;
  DECLARE user_id INT;

  SELECT SUM(WEIGHT) INTO uweight FROM projects;
  SELECT COUNT(id) INTO len FROM users;

  label1: LOOP
  SELECT id INTO user_id FROM users LIMIT i, i + 1;

  SELECT SUM(projects.weight * corrections.score) INTO weightSum FROM users 
  INNER JOIN corrections
  INNER JOIN projects
  ON
  (corrections.project_id = projects.id AND users.id = corrections.user_id)
  WHERE users.id = user_id;

  UPDATE users SET average_score = (weightSum / uweight) 
  WHERE 
  id = user_id;

  SET i = i + 1;
  IF i >= len
    THEN
    LEAVE label1;
  END LOOP;
END$$ 
