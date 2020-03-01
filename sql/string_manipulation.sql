--https://www.codewars.com/kata/594323fde53209e94700012a

SELECT
CASE
  WHEN 
    LENGTH(name) - LENGTH(REPLACE(name, ' ', '')) > 2 
      THEN CONCAT(SPLIT_PART(name, ' ', 1), ' ', SPLIT_PART(name, ' ', 2))
  ELSE SPLIT_PART(name, ' ', 1) END as name,
  
CASE
  WHEN LENGTH(name) - LENGTH(REPLACE(name, ' ', '')) > 2 
    THEN SPLIT_PART(name, ' ', 3) 
  ELSE SPLIT_PART(name, ' ', 2) END as first_lastname,
  
CASE
  WHEN LENGTH(name) - LENGTH(REPLACE(name, ' ', '')) > 2 
    THEN SPLIT_PART(name, ' ', 4) 
  ELSE SPLIT_PART(name, ' ', 3) END as second_lastname

FROM people