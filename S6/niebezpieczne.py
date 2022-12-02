mojkod = '''
a=5
b=4
print(f'axb= {a*b}')
'''

exec(mojkod)

import os
# code = input('co robisz dziś wieczorem?... ')
# exec(code)

def calcPerimeter(l):
    return 4*l

def calcArea(l):
    return l**2

expression = input("podaj funckję...")

for l in range(1,5):
    if(expression == 'calcPerimeter(l)'):
        print(f"jeśli długość jest równa {l} obwód wynosi: {eval(expression)}")
    elif (expression == 'calcArea(l)'):
        print(f"jeśli długość jest równa {l} pole wynosi: {eval(expression)}")
    else:
        print('zła funkcja')
        break
