import pandas as pd
import xlsxwriter


df = pd.DataFrame({'Data':[10,23,45,66,78,90,98,100,120,140,160,200]})

writer = pd.ExcelWriter('pd_dane.xlsx',engine='xlsxwriter')
