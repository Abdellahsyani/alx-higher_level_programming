-- cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
-- display the number of records
SELECT COUNT(id) 
FROM first_table
WHERE id = 89;
