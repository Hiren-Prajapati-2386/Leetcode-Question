import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = product.merge(right=sales,how="inner",on="product_id")

    grouped = df.groupby(by=['product_id','product_name'])['sale_date'].agg( 
                                                    min_date="min",
                                                   max_date="max").reset_index()

    mask = (grouped["min_date"] >= "2019-01-01") & (grouped["max_date"] <= "2019-03-31")

    return grouped[mask][['product_id','product_name']]
    