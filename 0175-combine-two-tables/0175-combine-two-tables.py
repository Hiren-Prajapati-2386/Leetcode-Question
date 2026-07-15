import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    df_result = pd.merge(person,address,on = "personId",how = "left")

    return df_result[['firstName','lastName','city','state']]
    