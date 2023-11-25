-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql
SELECT tv_genres.name AS genre,COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY genre ORDER BY number_of_shows DESC;