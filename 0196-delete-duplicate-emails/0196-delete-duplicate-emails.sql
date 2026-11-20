# Write your MySQL query statement below

with Output as (
    select * ,
    dense_rank() over(partition by email order by id asc) as rn
    from Person
)

delete from Person
where id in (select id from Output where rn > 1)