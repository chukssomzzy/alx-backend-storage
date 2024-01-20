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
  DECLARE i, j INT DEFAULT 0; 
  DECLARE len INT;
  DECLARE user_id INT;

  SELECT SUM(WEIGHT) INTO uweight FROM projects;
  SELECT COUNT(id) INTO len FROM users;

  loop_label: LOOP
  SET i = j; 
  SET j = j + 1;
  SELECT id INTO user_id FROM users LIMIT i, j;

  SELECT SUM(projects.weight * corrections.score) INTO weightSum FROM users 
  INNER JOIN corrections
  INNER JOIN projects
  ON
  (corrections.project_id = projects.id AND users.id = corrections.user_id)
  WHERE users.id = user_id;

  UPDATE users SET average_score = (weightSum / uweight) 
  WHERE 
  id = user_id;

  IF i >= len
    THEN
    LEAVE loop_label;
  END IF;
END LOOP loop_label;
END$$ 
