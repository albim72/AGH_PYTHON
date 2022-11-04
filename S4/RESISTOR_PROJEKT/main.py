from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

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

print("_____________________________________")
print("klasa Resistor")

r1 = Resistor(50E3)
r1.ohms = 10E3
print(r1.ohms)

print(f"układ elektryczny:\nopornik {r1.ohms} Om\nnapięcie prądu: {r1.voltage} V\n"
      f"natężenie prądu:{r1.current} A")

print("_____________________________________")
print("klasa VoltageResistance")

r2 = VoltageResistance(1.2E3)
print(f'natężenie początkowe prądu: {r2.current} A')
r2.voltage = 25
print(f'natężenie prądu: {r2.current} A')
print(f"napięcie prądu: {r2.voltage} V")
