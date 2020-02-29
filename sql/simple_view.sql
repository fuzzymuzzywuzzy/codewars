CREATE VIEW members_approved_for_voucher AS
  SELECT s.member_id id, m.name, m.email, sum(p.price) total_spending FROM sales s
  LEFT JOIN products p
  ON s.product_id = p.id
  LEFT JOIN members m 
  ON s.member_id = m.id
  WHERE 1 = 1
  AND s.department_id IN (
    SELECT s.department_id FROM sales s 
    LEFT JOIN departments d
    ON s.department_id = d.id
    LEFT JOIN products p
    ON s.product_id = p.id 
    GROUP BY s.department_id
    HAVING sum(p.price) > 10000)
  GROUP BY s.member_id, m.name, m.email
  HAVING sum(p.price) > 1000
  ORDER BY s.member_id ASC;

SELECT * FROM members_approved_for_voucher