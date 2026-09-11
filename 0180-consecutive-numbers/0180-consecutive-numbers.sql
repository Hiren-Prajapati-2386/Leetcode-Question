# Write your MySQL query statement below

select DISTINCT A.num as ConsecutiveNums from Logs as A
inner join Logs as B on A.id + 1 = B.id
inner Join Logs as C on B.id + 1 = C.id
where A.num = B.num and B.num = C.num