import pandas as pd
import datetime as dt
import numpy as np
import os

PRICE_LOCATION = os.path.join("dict", "price.csv")
DATA_LOCATION = os.path.join("data")
SHOP_LIST = [1, 2, 3, 4]
COUNTER_LIST = [1, 2, 3]
ITEMS = pd.read_csv(PRICE_LOCATION, sep=';')
DF_TEMPLATE = pd.DataFrame(
    data=[],
    columns=['itemid', 'amount', 'discount']
)
CUR_DATE = dt.date.today()
DISCOUNT_LIST = [0] * 10 + [.05] * 3 + [.1] * 2 + [.2] * 1
AMOUNT_DIST = np.clip(np.random.geometric(.5, 100), 1, 20)
print(AMOUNT_DIST)


for shop in SHOP_LIST:
    for counter in COUNTER_LIST:
        file_name = f'{shop}_{counter}_{dt.date.strftime(CUR_DATE, '%Y-%m-%d')}.csv'
        rand_rows = np.random.randint(5, 25)
        df = DF_TEMPLATE.copy()
        for i in range(rand_rows):
            item_id = np.random.choice(ITEMS['id'])
            df.loc[i, ['itemid', 'amount', 'discount']] = (
                np.random.choice(ITEMS['id']),
                np.random.choice(AMOUNT_DIST),
                np.random.choice(DISCOUNT_LIST)
                )
        df.to_csv(os.path.join(DATA_LOCATION, file_name))
