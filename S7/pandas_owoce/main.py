import pandas as pd

owoce = {
    'jabłko':[5,4,8,1],
    'pomarańcza':[4,3,5,2],
    'gruszka':[2,7,2,7],
    'winogrono':[13,16,10,44]
}

dane = pd.DataFrame(owoce)
print(dane)

dane = pd.DataFrame(owoce,index=['Jasio','Anna','Henio','Ola'])
print(dane)

print(dane.loc['Jasio'])

dane.to_csv('owocki.csv')
print(dane.info())
