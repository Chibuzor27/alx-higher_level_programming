-- List cities in Cali
SELECT id, name FROM cities
WHERE state_id IN (
	SELECT id FROM states
	WHERE NAME = 'California')
ORDER BY id DESC
