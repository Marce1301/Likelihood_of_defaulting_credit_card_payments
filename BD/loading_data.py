# declare libraries used in this program
import mysql.connector
import numpy as np
import pandas as pd
from pathlib import Path


# you must have a file config.py with the credencialts to access de DB
from config import u_key, p_key, host_key, BD_key


# Read the CSV file from the Resources folder into a Pandas DataFrame


df = pd.read_excel('..\BD\data_upload.xlsx', engine='openpyxl', header=0)
df.head()



# you must have your credencials to connect to the BD, ask Ale for information
cnx = mysql.connector.connect(user=u_key,
                              password=p_key,
                              host=host_key,
                              database=BD_key)

for n, row in df.iterrows():

    # 25 values, one per each table field
    insert_ = (f"INSERT INTO  credit_card_prediction (ID,\
        LIMIT_BAL,\
        SEX,\
        EDUCATION,\
        MARRIAGE,\
        AGE,\
        PAYMENT_SEPTEMBER_2005,\
        PAYMENT_AUGUST_2005,\
        PAYMENT_JUL_2005,\
        PAYMENT_JUN_2005,\
        PAYMENT_MAY_2005,\
        PAYMENT_APRIL_2005,\
        AMOUNT_OF_BILL_SEPTEMBER_2005,\
        AMOUNT_OF_BILL_AUGUST_2005,\
        AMOUNT_OF_BILL_JUL_2005,\
        AMOUNT_OF_BILL_JUN_2005,\
        AMOUNT_OF_BILL_MAY_2005,\
        AMOUNT_OF_BILL_APRIL_2005,\
        AMOUNT_PREVIOUS_PAY_SEPTEMBER_2005,\
        AMOUNT_PREVIOUS_PAY_AUGUST_2005,\
        AMOUNT_PREVIOUS_PAY_JUL_2005,\
        AMOUNT_PREVIOUS_PAY_JUN_2005,\
        AMOUNT_PREVIOUS_PAY_MAY_2005,\
        AMOUNT_PREVIOUS_PAY_APRIL_2005,\
        DEFAULT_PAYMENT_NEXT_MONTH) values (\
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    # build the secord part of INSERT STATEMENT with row data 
    data_insert = (row["ID"],\
            row["LIMIT_BAL"],\
            row["SEX"],\
            row["EDUCATION"],\
            row["MARRIAGE"],\
            row["AGE"],\
            row["PAY_0"],\
            row["PAY_2"],\
            row["PAY_3"],\
            row["PAY_4"],\
            row["PAY_5"],\
            row["PAY_6"],\
            row["BILL_AMT1"],\
            row["BILL_AMT2"],\
            row["BILL_AMT3"],\
            row["BILL_AMT4"],\
            row["BILL_AMT5"],\
            row["BILL_AMT6"],\
            row["PAY_AMT1"],\
            row["PAY_AMT2"],\
            row["PAY_AMT3"],\
            row["PAY_AMT4"],\
            row["PAY_AMT5"],\
            row["PAY_AMT5"],\
            row["default_payment_next_month"])


    cursor_insert = cnx.cursor(buffered=True)

    # execute the INSERT, with the row data into the table credit_card_prediction
    cursor_insert.execute(insert_,(data_insert))

    print(f"{n} rows")
    if (n%50==0):
        cnx.commit()  # commit into the DB to save the data

cnx.commit()  # commit into the DB to save the new data

cursor_insert.close()
cnx.close()
