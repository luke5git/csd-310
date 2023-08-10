#Last minute changes to SQL Programming for various locations and changes to wishlists behaviors for users.
#Luke Wilkins, 08-09-2023, CYBR410-T301
SHOW TABLES;
SELECT * FROM store;
DROP TABLE IF EXISTS store;
CREATE TABLE store(
store_id INT NOT NULL PRIMARY KEY,
locale VARCHAR(500) NOT NULL,
city VARCHAR(50) NOT NULL,
hours VARCHAR(50) NOT NULL );

INSERT INTO store(store_id, locale, city, hours)
VALUES (1, 'Mandolin Books', "Oklahoma City", "10:00 A.M. to 6:00 P.M."),
(2, "Mandolin Books", "Moore City", "10:00 A.M. to 6:00 P.M.");
SELECT * FROM wishlist;
SELECT user.user_id, first_name, last_name, book_name FROM user
INNER JOIN wishlist ON user.user_id = wishlist.user_id
INNER JOIN book ON book.book_id = wishlist.book_id;

SELECT * FROM user
INNER JOIN wishlist ON user.user_id = wishlist.user_id
INNER JOIN book ON book.book_id = wishlist.book_id;

SELECT * FROM wishlist;
SELECT * FROM book
LEFT JOIN wishlist ON book.book_id = wishlist.book_id;
-- WHERE user_id != 1;
SELECT book_id, book_name FROM book
WHERE book_id NOT IN ( SELECT book_id FROM wishlist WHERE user_id
= 1);

SHOW TABLES;
SELECT * FROM store;