Using MySQL,design a database whose name is IMDB.Create proper MYSQL tables, Primary Key, Foreign Key, add data into the MySQL tables and do the following as given below:-

1.Movie should have multiple media(Video or Image)
2.Movie can belongs to multiple Genre.
3.Movie can have multiple reviews and Review can belongs to a user.
4.Artist can have multiple skills.
5.Artist can perform multiple role in a single film.

CREATE TABLE Movie (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    release_date DATE,
    description TEXT
);

CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE Movie_Genre (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

CREATE TABLE Review (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    movie_id INT,
    user_id INT,
    rating DECIMAL(3,1),
    review_text TEXT,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100)
);

CREATE TABLE Artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Skill (
    skill_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE Artist_Skill (
    artist_id INT,
    skill_id INT,
    PRIMARY KEY (artist_id, skill_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (skill_id) REFERENCES Skill(skill_id)
);

CREATE TABLE Role (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE Movie_Artist (
    movie_id INT,
    artist_id INT,
    role_id INT,
    PRIMARY KEY (movie_id, artist_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id),
    FOREIGN KEY (role_id) REFERENCES Role(role_id)
);

CREATE TABLE Media (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    type ENUM('Video', 'Image') NOT NULL,
    url VARCHAR(255) NOT NULL,
    movie_id INT,
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id)
);

-- Inserting sample movies
INSERT INTO Movie (title, release_date, description) VALUES
('The Shawshank Redemption', '1994-09-10', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'),
('The Godfather', '1972-03-24', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'),
('The Dark Knight', '2008-07-18', 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.');

-- Inserting sample genres
INSERT INTO Genre (name) VALUES
('Drama'),
('Crime'),
('Action');

-- Associating movies with genres
INSERT INTO Movie_Genre (movie_id, genre_id) VALUES
(1, 1), -- The Shawshank Redemption - Drama
(2, 1), -- The Godfather - Drama
(2, 2), -- The Godfather - Crime
(3, 1), -- The Dark Knight - Drama
(3, 3); -- The Dark Knight - Action

-- Inserting sample users
INSERT INTO User (username, email) VALUES
('user1', 'user1@example.com'),
('user2', 'user2@example.com');

-- Inserting sample artists
INSERT INTO Artist (name) VALUES
('Tim Robbins'),
('Morgan Freeman'),
('Marlon Brando'),
('Al Pacino'),
('Christian Bale'),
('Heath Ledger');

-- Inserting sample skills
INSERT INTO Skill (name) VALUES
('Acting'),
('Directing');

-- Associating artists with skills
INSERT INTO Artist_Skill (artist_id, skill_id) VALUES
(1, 1), -- Tim Robbins - Acting
(2, 1), -- Morgan Freeman - Acting
(3, 1), -- Marlon Brando - Acting
(4, 1), -- Al Pacino - Acting
(5, 1), -- Christian Bale - Acting
(5, 2), -- Christian Bale - Directing
(6, 1); -- Heath Ledger - Acting

-- Inserting sample roles
INSERT INTO Role (name) VALUES
('Actor'),
('Director');

-- Associating artists with roles in movies
INSERT INTO Movie_Artist (movie_id, artist_id, role_id) VALUES
(1, 1, 1), -- Tim Robbins acted in The Shawshank Redemption
(1, 2, 1), -- Morgan Freeman acted in The Shawshank Redemption
(2, 3, 1), -- Marlon Brando acted in The Godfather
(2, 4, 1), -- Al Pacino acted in The Godfather
(3, 5, 1), -- Christian Bale acted in The Dark Knight
(3, 6, 1); -- Heath Ledger acted in The Dark Knight

-- Inserting sample reviews
INSERT INTO Review (movie_id, user_id, rating, review_text) VALUES
(1, 1, 9.3, 'One of the best movies ever made.'),
(1, 2, 9.5, 'A masterpiece of storytelling.'),
(2, 1, 9.5, 'The Godfather is a classic.'),
(3, 2, 9.8, 'Heath Ledger delivers an iconic performance.');

-- Inserting sample media
INSERT INTO Media (type, url, movie_id) VALUES
('Image', 'shawshank_redemption.jpg', 1),
('Image', 'godfather.jpg', 2),
('Image', 'dark_knight.jpg', 3);
