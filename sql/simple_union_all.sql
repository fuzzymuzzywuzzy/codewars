--https://www.codewars.com/kata/58112f8004adbbdb500004fe

SELECT 'US' AS location, 
us.id,
us.name, 
us.price,
us.card_name,
us.card_number,
us.transaction_date
FROM ussales us
WHERE us.price > 50
GROUP BY 1,2,3,4,5,6

UNION ALL 

SELECT 'EU' as location,
eu.id,
eu.name, 
eu.price,
eu.card_name,
eu.card_number,
eu.transaction_date
FROM eusales eu
WHERE eu.price > 50
GROUP BY 1,2,3,4,5,6

ORDER BY location DESC, id ASC