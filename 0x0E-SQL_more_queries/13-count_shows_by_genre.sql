-- List genres
SELECT name AS genre, count(*) AS number_of_shows FROM tv_show_genres a
JOIN tv_genres b ON a.genre_id = b.id
GROUP BY genre
ORDER BY number_of_shows DESC
