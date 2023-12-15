-- List genres (Dexter)
SELECT c.name FROM tv_shows a
JOIN tv_show_genres b ON a.id = b.show_id
JOIN tv_genres c ON b.genre_id = c.id
WHERE title = 'Dexter'
ORDER BY genre;
