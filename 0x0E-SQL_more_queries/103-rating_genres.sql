-- List genre rating
SELECT name, sum(rate) AS rating FROM tv_genres a
JOIN tv_show_genres b ON a.id = b.genre_id
JOIN tv_shows c ON c.id = b.show_id 
JOIN tv_show_ratings d ON d.show_id = c.id
GROUP BY name
ORDER BY rating DESC
