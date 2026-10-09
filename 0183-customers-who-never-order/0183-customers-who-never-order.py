import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    no_order = customers.merge(
        orders,
        how='left',
        left_on='id',
        right_on='customerId'
    )

    result = no_order[no_order['customerId'].isna()][['name']]
    result.columns = ['Customers']

    return result