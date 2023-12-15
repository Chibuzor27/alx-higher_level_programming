-- List cities and states
SELECT a.id, a.name, b.name FROM cities a
JOIN states b on a.state_id = b.id
ORDER BY a.id
