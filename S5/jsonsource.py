import json

x = '{"name":"Jan","age":34,"city":"Kraków","room nb":6}'

print(x)
print(type(x))

osoba = json.loads(x)
print(osoba)
print(type(osoba))

print(f"wiek osoby: {osoba['age']}")
