-- a script that dispalys the top 3 cities temp
SELECT city, temperature FROM your_table_name WHERE MONTH(date) IN(7, 8) ORDER BY temperature DESC LIMIT 3;
