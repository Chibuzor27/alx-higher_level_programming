-- List shows
SELECT title, genre_id FROM tv_shows a
LEFT OUTER JOIN tv_show_genres b ON a.id = b.show_id 
ORDER BY title, genre_id
