import json

x = '{"names":["Jan","Karol","Leon"],"age":34,"city":"Kraków","room nb":6}'

print(x)
print(type(x))

osoba = json.loads(x)
print(osoba)
print(type(osoba))

print(f"wiek osoby: {osoba['age']}")
print(f"drugie imię: {osoba['names'][1]}")

samochod = {
    "marka":"Opel",
    "model":"Insignia",
    "poj":1.9,
    "rocznik":2019
}

jsonsam = json.dumps(samochod,indent=4)
print(jsonsam)
print(type(jsonsam))

with open("samochod.json","w",encoding="utf-8") as f:
    f.write(jsonsam)


with open("samochod.json","r",encoding="utf-8") as f:
    auto_dict = json.load(f)

print(auto_dict)
