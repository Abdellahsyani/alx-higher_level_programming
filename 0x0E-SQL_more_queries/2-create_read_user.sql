-- 2-create_read_user.sql | mysql -hlocalhost -uroot -p
-- creates the databases
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'uesr_0d_2'@'localhost';
