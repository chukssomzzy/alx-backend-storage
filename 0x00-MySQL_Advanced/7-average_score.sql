-- Compute Average Score 

--  Average Score For user
DELIMITER $$
CREATE PROCEDURE computeAverageScoreForUser(IN user_id INT)
LANGUAGE SQL
COMMENT 'Average corrections score' 
CONTAINS SQL 
NOT DETERMINISTIC 
SQL SECURITY DEFINER 
BEGIN 
  DECLARE u_avg_score FLOAT; 

  SELECT AVG(score) INTO u_avg_score 
  FROM corrections 
  WHERE corrections.user_id = user_id;

  UPDATE users 
  SET average_score = u_avg_score
  WHERE id = user_id; 
END$$
