-- List comedies
SELECT title FROM tv_genres a
JOIN tv_show_genres b ON a.id = b.genre_id
JOIN tv_shows c on b.show_id = c.id
WHERE a.name = 'Comedy'
ORDER BY title;
