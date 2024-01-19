-- COMPUTE WEIGHTED AVERAGR

-- Stored procedure
DELIMITER $$ 
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
LANGUAGE SQL
COMMENT 'Calculate average weighted score for a user'
NOT DETERMINISTIC
SQL SECURITY DEFINER
CONTAINS SQL
BEGIN
  DECLARE uweight INT;
  DECLARE weightSum INT;

  SELECT SUM(WEIGHT) INTO uweight FROM projects;

  SELECT SUM(projects.weight * corrections.score) INTO weightSum FROM users 
  INNER JOIN corrections
  ON 
  (users.id = corrections.user_id)
  INNER JOIN projects
  ON
  (corrections.project_id = projects.id);
  WHERE users.id = user_id;

  UPDATE users SET average_score = (uweight / weightSum) 
  WHERE 
  id = user_id; 
END$$

