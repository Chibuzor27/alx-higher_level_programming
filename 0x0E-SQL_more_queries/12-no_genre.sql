-- List shows without a genre
SELECT title, genre_id FROM tv_shows a
LEFT OUTER JOIN tv_show_genres b ON a.id = b.show_id AND genre_id = NULL
ORDER BY title, genre_id;
