-- Not my genres
SELECT name FROM tv_genres c 
WHERE c.id NOT IN (
	SELECT genre_id FROM tv_shows a
	JOIN tv_show_genres b ON a.id = b.show_id 
	WHERE title = 'Dexter')
ORDER BY name
