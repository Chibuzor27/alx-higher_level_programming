-- List shows by genre
SELECT title, name FROM tv_shows a
LEFT OUTER JOIN tv_show_genres b on a.id = b.show_id
LEFT OUTER JOIN tv_genres c on b.genre_id = c.id
ORDER BY title, name;
