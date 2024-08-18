import kaggle
import pandas as pd
import sqlalchemy as sal
# import zipfile
# zip_ref=zipfile.ZipFile('orders.csv.zip')
# zip_ref.extractall()
# zip_ref.close()
df=pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')

df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price']=df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
# print(df)

#convert order date from object data type to datetime
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


#drop cost price, list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)
# print(df)

#load the data into sql server using replace option
engine=sal.create_engine('')
conn=engine.connect()

#load the data into sql server using append option
df.to_sql('df_orders',con=conn,index=False,if_exists='append')



