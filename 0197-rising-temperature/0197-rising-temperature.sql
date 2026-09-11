

select A.id from weather as A
inner join weather as B
on datediff(A.recordDate,B.recordDate) = 1
where A.temperature > B.temperature;