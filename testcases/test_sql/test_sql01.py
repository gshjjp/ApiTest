import time
import os
import mysql.connector
from mysql.connector import Error
import pandas as pd
from openpyxl import load_workbook

try:
    with mysql.connector.connect(
            host='172.16.100.20',
            user='moushi',
            password='xKpj!p@9QK9C19mB',
            database='moushi_user'
    ) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT name, avatar, phone FROM t_staff WHERE gender = 1 AND name LIKE '%艳妮%' ORDER BY update_time DESC")
            rows = cursor.fetchall()
            print(rows)

            df = pd.DataFrame(rows, columns=['name', 'avatar', 'phone'])

            file_path = 'staff_data.xlsx'

            if os.path.exists(file_path):
                with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                    df.to_excel(writer, sheet_name='Sheet1', index=False, header=False,
                                startrow=writer.sheets['Sheet1'].max_row)
            else:
                df.to_excel(file_path, index=False)
                print("Excel file created.")

            print("----------success---------")
            time.sleep(5)

except Exception as e:
    print(f"Error: {e}")

print('-------------------chenggong--------------')
