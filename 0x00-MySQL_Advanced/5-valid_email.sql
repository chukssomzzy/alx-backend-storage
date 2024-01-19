-- More trigger 

-- Is valid email 
DELIMITER $$
CREATE TRIGGER isValidEmail
BEFORE UPDATE ON users 
FOR EACH ROW 
BEGIN
  IF OLD.email != NEW.email
    THEN
    SET NEW.valid_email = 0;
  END IF;
END$$
