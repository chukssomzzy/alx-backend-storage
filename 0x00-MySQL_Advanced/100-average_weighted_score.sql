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
  INNER JOIN projects
  ON
  (corrections.project_id = projects.id AND users.id = corrections.user_id)
  WHERE users.id = user_id;

  UPDATE users SET average_score = (weightSum / uweight) 
  WHERE 
  id = user_id; 
END$$
