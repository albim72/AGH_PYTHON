import pandas as pd
import xlsxwriter

df = pd.DataFrame({
    'Kraj':['Chiny','Indie','USA','Indonezja'],
    'Populacja':[1404338840,1366938189,330267997,269603400],
    'Pozycja':[1,2,3,4]
})

df = df[['Pozycja','Kraj','Populacja']]

writer = pd.ExcelWriter('populacja_kraje.xlsx', engine='xlsxwriter')
df.to_excel(writer,sheet_name='pop',startrow=1,header=False,index=False)

workbook = writer.book
worksheet = writer.sheets['pop']
(max_row,max_col) = df.shape
column_settings = [{'header':column} for column in df.columns]
worksheet.add_table(0,0,max_row,max_col-1,{'columns':column_settings})
worksheet.set_column(0,max_col-1,12)
writer.save()
