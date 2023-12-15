-- Not my genres
SELECT title FROM tv_shows c 
WHERE c.id NOT IN (
	SELECT show_id FROM tv_genres a
	JOIN tv_show_genres b ON a.id = b.genre_id 
	WHERE name = 'Comedy')
ORDER BY title
