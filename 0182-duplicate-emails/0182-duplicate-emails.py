import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:

    email_list = pd.DataFrame(person.loc[person['email'].duplicated(),'email'].unique().tolist(),columns = ['email'])

    return email_list
    