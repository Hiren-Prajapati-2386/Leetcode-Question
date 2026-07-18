/* Write your T-SQL query statement below */
select name as Customers from Customers as c
left join Orders as o
on c.id = o.customerId
where o.customerId is Null;