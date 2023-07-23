-- Luke Wilkins 07-23-2023
-- CYBR410 Professor Haas
-- DropSQL for table and users
-- Did not include in original code to avoid altering original code accidentally
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';
DROP USER IF EXISTS 'pysports_user'@'localhost';
DROP TABLE IF EXISTS player;