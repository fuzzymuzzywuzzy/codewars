--https://www.codewars.com/kata/593ef0e98b90525e090000b9

SELECT t.id, t.heads, t.arms, b.legs, b.tails,
CASE
WHEN t.heads > t.arms THEN 'BEAST' 
WHEN b.tails > b.legs THEN 'BEAST'
ELSE 'WEIRDO'
END AS species 
FROM top_half t
INNER JOIN bottom_half b
ON t.id = b.id 
ORDER BY species