-- usage: 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvsh
-- lists all shows contained
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows 
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_shows_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
