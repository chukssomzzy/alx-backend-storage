-- More trigger 

-- Is valid email 
DELIMITER $$
CREATE TRIGGER isValidEmail
AFTER UPDATE ON users 
FOR EACH ROW 
  BEGIN
    IF NEW.email AND OLD.email != NEW.email
      THEN
      SET NEW.valid_email = 0;
    END IF;
  END$$
