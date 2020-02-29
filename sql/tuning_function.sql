--https://www.codewars.com/kata/581fb63e70ca28d92500000d

WITH salary_incr AS 
(SELECT d.department_id, d.department_name, 1+pctIncrease(d.department_id) AS pct FROM departments d)

SELECT e.employee_id,
       e.first_name,
       e.last_name,
       s.department_name,
       e.salary AS old_salary,
       e.salary*s.pct AS new_salary
       
FROM employees e 
LEFT JOIN salary_incr s
ON e.department_id = s.department_id 
ORDER BY 1 ASC