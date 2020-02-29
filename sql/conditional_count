SELECT
EXTRACT(MONTH FROM payment_date) AS month,
COUNT(payment_id) AS total_count,
SUM(amount) as total_amount,
COUNT(CASE WHEN staff_id = 1 THEN payment_id END) AS mike_count,
SUM(CASE WHEN staff_id = 1 THEN amount END) AS mike_amount, 
COUNT(CASE WHEN staff_id = 2 THEN payment_id END) AS jon_count,
SUM(CASE WHEN staff_id = 2 THEN amount END) AS jon_amount

FROM payment

GROUP BY 1
ORDER BY 1 ASC 