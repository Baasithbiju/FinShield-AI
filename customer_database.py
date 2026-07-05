import pandas as pd
import os

FILE_NAME = "customer_records.xlsx"

def save_customer(customer_data):

    if os.path.exists(FILE_NAME):
        df = pd.read_excel(FILE_NAME)
    else:
        df = pd.DataFrame()

    df = pd.concat(
        [df, pd.DataFrame([customer_data])],
        ignore_index=True
    )

    df.to_excel(FILE_NAME, index=False)


def load_customers():

    if os.path.exists(FILE_NAME):
        return pd.read_excel(FILE_NAME)

    return pd.DataFrame()