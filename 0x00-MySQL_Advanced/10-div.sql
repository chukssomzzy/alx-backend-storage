-- SAFE DIV 

-- RETURN a / b or if b == 0 0
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
  DECLARE udiv FLOAT;
  IF b = 0 or ISNULL(b)
    THEN
    RETURN 0;
  END IF
  SET udiv = (a / b);
  RETURN udiv;
END$$
