# Write your MySQL query statement below

with newTabel as(
    select D.name as Department,E.name as Employee,E.salary Salary,
    dense_rank() over(partition by E.departmentId order by salary desc) as rn
    from Employee as E
    inner join Department as D
    on E.departmentId = D.id
)

select Department,Employee,Salary from newTabel
where rn in (1,2,3);