#Luke Wilkins -- Module 10.3 Assignment
#Professor Haas -- CYBR410-T301

CREATE TABLE user(
user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(75) NOT NULL,
Last_name VARCHAR(75) NOT NULL);

CREATE TABLE book(
book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
book_name VARCHAR(200) NOT NULL, 
details VARCHAR(500), 
author VARCHAR(200) NOT NULL);

CREATE TABLE wishlist(
wishlist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL,
book_id INT NOT NULL, 
FOREIGN KEY(user_id) REFERENCES user(user_id),
FOREIGN KEY(book_id) REFERENCES book(book_id));

CREATE TABLE store(
store_id INT NOT NULL PRIMARY KEY,
locale VARCHAR(500) NOT NULL);

INSERT INTO store(store_id, locale)
VALUES (1, 'Mandolin Books');

INSERT INTO book(book_name, details, author)
VALUES('Harry Potter and the Chamber of Secrets', 'Harry Potter uncovers the dark secrets of Hogwarts School for Magic', 'J.K. Rowling'),
('Gone With the Wind', 'A Southern belle and a rouguish profiteer face off in a turbulent romance as the society around them crumbles', 'Margaret Mitchell'),
('Dead Lions', 'Dishonored agents with MI5 uncover a lethal Cold War-era legacy of sleeper cells and mythic super spies', 'Mick Herron'),
('Task Force Desperate', 'A small band of mercenaries are called in to conduct reconnaissance after a US base in Africa is overrun', 'Tom Clancy'),
('Escalation', 'A hostage in Slovakia needs to be saved without being detected', 'Peter Nealen'),
('Flash Point', 'Unknown enemies are bent on creating tension in peaceful regions', 'Tom Clancy'),
('Chain of Command', 'A secretive billionaire uses his wealth to further his corrupt ambitions', 'Tom Clancy'),
('Beast Three Six', 'A senators daughter is kidnapped by a terrorist', 'Jason Kasper'),
('The Enemies of My Country', 'A former Army Ranger and his team of mercenaries hunt down a terrorist', 'Jason Kasper');

INSERT INTO user(first_name, Last_name)
VALUES('Richard', 'Martin'),
('Matilda', 'Wild'),
('Patrick', 'Ewing');

INSERT INTO wishlist(user_id, book_id)
VALUES(1, 7),
(2, 4),
(3, 1);