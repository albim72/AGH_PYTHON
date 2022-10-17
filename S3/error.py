try:
    y = 5
    print(x)
except NameError:
    print("x nie jest zdefiniowany!")
except:
    print("błąd nieokreślony")
else:
    print(f'y={y}')
finally:
    x_1=10
    print(f"wartość x_1 wynosi {x_1}")

print("ciąg dalszy")
