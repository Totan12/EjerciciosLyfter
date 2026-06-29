celsius = float(input("Ingrese una temperatura en celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = 273.15 + celsius
print(
f"""
=======================
Celsius: {celsius}
Fahrenheit: {fahrenheit}
Kelvin: {kelvin}
=======================
"""
)