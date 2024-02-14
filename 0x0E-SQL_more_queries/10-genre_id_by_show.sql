-- 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvsh
-- list all rowsof a database
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
	INNER
	JOIN tv_show_genres 
	ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC,
	tv_show_genres.genre_id ASC;
