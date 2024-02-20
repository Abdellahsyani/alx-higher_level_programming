-- convert databases to utf-8
-- khdam azmar baraka n t3nkich
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
