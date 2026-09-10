CREATE DATABASE netflix_project;


CREATE TABLE netflix_titles (
    show_id TEXT,
    type TEXT,
    title TEXT,
    director TEXT,
    cast_members TEXT,
    country TEXT,
    date_added TEXT,
    release_year INT,
    rating TEXT,
    duration TEXT,
    listed_in TEXT,
    description TEXT
);

SELECT *
FROM netflix_titles
LIMIT 10;

SELECT
COUNT(*) - COUNT(director) AS missing_director,
COUNT(*) - COUNT(cast_members) AS missing_cast,
COUNT(*) - COUNT(country) AS missing_country,
COUNT(*) - COUNT(rating) AS missing_rating
FROM netflix_titles;

-- Movies vs TV Shows

SELECT type,
COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY type
ORDER BY total_titles DESC;


-- Top countries producing content

SELECT country,
COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;

-- Titles per release year

SELECT  release_year,
COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year
ORDER BY release_year;

-- Rating distribution

SELECT rating,
COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY rating
ORDER BY total_titles DESC;

-- Movies vs TV Shows per release year

SELECT release_year,
	   type,
COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year, type
ORDER BY release_year;

-- Top genrres

SELECT listed_in,
COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY listed_in
ORDER BY total_titles DESC 
LIMIT 10;

-- Top directors

SELECT director,
COUNT(*) AS total_titles
FROM netflix_titles 
WHERE director IS NOT NULL
GROUP BY DIRECTOR
ORDER BY total_titles DESC
LIMIT 10;

-- Rating distribution (Movies)

SELECT rating,
COUNT(*) AS total_movies
FROM netflix_titles
WHERE type='Movie'
GROUP BY rating
ORDER BY total_movies DESC;

-- Most recent content

SELECT title,
	   release_year,
	   type
FROM netflix_titles 
ORDER BY release_year DESC
LIMIT 10;
	
