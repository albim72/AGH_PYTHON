import os

f = open("dane.txt","r",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print("________________________________")

f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()

print("________________________________")

f = open("dane.txt","r",encoding="utf-8")
for x in f:
    print(x)
f.close()

print("_______________tworzenie nowego pliku_________________")

f = open("message.txt","a",encoding="utf-8")
f.write("to jest linia z ważną informacją: fhjowejfoejfe \n")
f.close()

f = open("message.txt","r",encoding="utf-8")
print(f.read())
f.close()

print("_______________usuwanie pliku_________________")

if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("plik został usunięty")
else:
    print("plik nie istnieje")
