--https://www.codewars.com/kata/594257d4db68b6e99200002c

SELECT project, 
REGEXP_REPLACE(address,'[[:digit:]]','','g') as letters, 
REGEXP_REPLACE(address,'[[:alpha:]]','','g') as numbers
FROM repositories