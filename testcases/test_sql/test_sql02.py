# _*_ coding : utf-8 _*_
# @Time : 2024/11/22 下午2:06
# @Author : 耿
# @File : test_sql02
# @Project :
import  os

import mysql.connector
import pandas as pd
import requests


image_folder = 'downloaded_avatars'
os.makedirs(image_folder, exist_ok=True)


host = os.getenv('DB_HOST','172.16.100.20')
user = os.getenv('DB_USER','moushi')
password = os.getenv('DB_PASSWORD','xKpj!p@9QK9C19mB')
database = os.getenv('DB_DATABASE','moushi_user')




with mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
) as conn:
    with conn.cursor() as cursor:
        query = '''
        SELECT name, avatar, phone FROM t_staff WHERE gender = 1 AND name LIKE '%佳艺%' ORDER BY update_time DESC
        '''

        cursor.execute(query)
        rows = cursor.fetchall()

        print(rows)


        df = pd.DataFrame(rows,columns=['name','avatar','phone'])
        print(df)
        for index , rows in df.iterrows():
            avatar_url = rows['avatar']
            print(index)
            print('--------------------')
            print(rows)
            if avatar_url:
                try:
                    response = requests.get(avatar_url,stream=True)
                    if response.status_code == 200:
                        img_name = f"{rows['name']}_{index}.jpg".replace("/","_")
                        # print(img_name)
                        img_path = os.path.join(image_folder,img_name)
                        with open(img_path,'wb') as file:
                            for chunk in response.iter_content(1024):
                                file.write(chunk)
                            print(f"download:{img_name}")
                    else:
                        print(f"cuowude:{avatar_url}")


                except Exception as e:
                    print("--------error--------")
            else:
                print(f"wuyou{rows['avatar']}")



