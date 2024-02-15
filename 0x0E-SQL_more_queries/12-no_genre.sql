--  lists all shows contained in hbtn_0d_tvshows without a genre linked
-- lists all rows of a database that don't have one column
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows 
LEFT JOIN tv_shows_genres
ON tv_showa.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
