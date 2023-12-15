-- List shows by genre id
SELECT title, genre_id FROM tv_shows a
JOIN tv_show_genres b ON a.id = b.show_id 
ORDER BY title, genre_id;
