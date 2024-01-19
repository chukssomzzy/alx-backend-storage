-- CREATE VIEW 

-- NEED MEETING 
CREATE VIEW need_meeting
AS
SELECT * FROM students 
WHERE score < 80 
AND 
(ISNULL(last_meeting) 
  OR last_meeting < ADDDATE(CURDATE(), INTERVAL -1 MONTH));
