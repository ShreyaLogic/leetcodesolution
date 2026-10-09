import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lowfat_recyclable_filter = (
        (products['low_fats'] == 'Y') &
        (products['recyclable'] == 'Y')
    )

    return products.loc[lowfat_recyclable_filter, ['product_id']]