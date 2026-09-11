CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      with newTable as (
        select *, dense_rank() over(order by salary desc) as rn
        from Employee
      )
    
    select (
      select salary
      from newTable
      where rn = N
      limit 1
    ) as getNthHighestSalary
  );
END