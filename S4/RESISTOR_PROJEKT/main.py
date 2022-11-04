from oldresistor import OldResistor

print("_____________________________________")
print("klasa OldResistor")
r0 = OldResistor(10.2E2)
print(r0)
print(r0._ohms)
r0._ohms = 2.88E3
print(r0._ohms)
print(r0.get_ohms())
r0.set_ohms(4.5E2)
print(r0.get_ohms())
