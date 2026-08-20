
with second_highest as (
    select salary as SecondHighestSalary, dense_rank() over(order by salary desc) as rn
    from Employee
)

select (
select SecondHighestSalary from second_highest
where rn = 2
limit 1
) as SecondHighestSalary;