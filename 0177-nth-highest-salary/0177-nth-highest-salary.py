import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    unique_rows = employee.drop_duplicates(subset=['salary'])

    if N <= 0 or N > unique_rows.shape[0]:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    NthSalary = unique_rows['salary'].sort_values(ascending=False).iloc[N-1]

    return pd.DataFrame({f"getNthHighestSalary({N})" : [NthSalary]})

