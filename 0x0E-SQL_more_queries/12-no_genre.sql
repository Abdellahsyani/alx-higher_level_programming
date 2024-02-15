-- import database dump
-- lists all shows contained
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows RIGHT JOIN tv_shows_genres
ON tv_showa.id = tv_show_genres.show_id
ORDER BY tv_showa.title ASC,
	tv_show_genres.genre_id ASC;
