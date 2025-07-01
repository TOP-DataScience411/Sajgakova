--ЗАПРОСЫ К ТАБЛИЦЕ COUNTRY
-- 1. Вывести названия всех стран Евразии
SELECT Name
FROM country
WHERE Continent IN ('Europe', 'Asia');

-- 2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет
SELECT Region, Name
FROM country
WHERE LifeExpectancy < 50;

-- 3. Вывести название самой крупной по площади страны Африки
SELECT Name
FROM country
WHERE Continent = 'Africa'
ORDER BY SurfaceArea DESC
LIMIT 1;

-- 4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
SELECT Name
FROM country
WHERE Continent = 'Asia'
ORDER BY (Population / SurfaceArea) ASC
LIMIT 5;

--ЗАПРОСЫ К ТАБЛИЦЕ CITY
-- 5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек
SELECT CountryCode, Name
FROM city
WHERE Population > 5000000
ORDER BY Population ASC;

-- 6. Вывести название города в Индии с самым длинным названием
SELECT Name
FROM city
WHERE CountryCode = (SELECT Code FROM country WHERE Name = 'India')
ORDER BY CHAR_LENGTH(Name) DESC
LIMIT 1;