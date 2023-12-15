-- List rating
SELECT title, sum(rate) AS rating FROM tv_shows a
JOIN tv_show_ratings b ON a.id = b.show_id
GROUP BY title
ORDER BY rating DESC
