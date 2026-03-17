def celc_to_far(c):
    return (c * 9/5) + 32

def far_to_celc(f):
    return (f - 32) * 5/9

def celc_to_kelvin(c):
    return c + 273.15

def kelvin_to_celc(k):
    return k - 273.15

def far_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_far(k):
    return (k - 273.15) * 9/5 + 32


def feet_to_meter(f):
    return f * 0.3048

def meter_to_feet(m):
    return m / 0.3048


def kg_to_pound(kg):
    return kg * 2.20462

def pound_to_kg(lb):
    return lb / 2.20462



print("""
1) Temparature
2) Height 
3) Weight
""")

choice = int(input("What type of convert you want? 1/2/3   ▶️  "))

if choice == 1:
    print("""
    1) Celcius to Farenheit
    2) Farenhrit to celcius
    3) Celcius to Kelvin
    4) Kelvin to Celcius
    5) Farenheit to Kelvin 
    6) Kelvin to Farenheit
    """)
    choice_temp = int(input("Enter your choice :  "))

    if choice_temp == 1:
        temp = float(input("Enter temperature in Celcius: "))
        print(celc_to_far(temp))

    elif choice_temp == 2:
        temp = float(input("Enter temperature in Farenheit: "))
        print(far_to_celc(temp))

    elif choice_temp == 3:
        temp = float(input("Enter temperature in Celcius: "))
        print(celc_to_kelvin(temp))

    elif choice_temp == 4:
        temp = float(input("Enter temperature in Kelvin: "))
        print(kelvin_to_celc(temp))

    elif choice_temp == 5:
        temp = float(input("Enter temperature in Farenheit: "))
        print(far_to_kelvin(temp))

    elif choice_temp == 6:
        temp = float(input("Enter temperature in Kelvin: "))
        print(kelvin_to_far(temp))


elif choice == 2:
    print("""
    1) Feet to Meter
    2) Meter to Feet
    """)
    choice_height = int(input("Enter your choice :  "))

    if choice_height == 1:
        val = float(input("Enter value in Feet: "))
        print(feet_to_meter(val))

    elif choice_height == 2:
        val = float(input("Enter value in Meter: "))
        print(meter_to_feet(val))


elif choice == 3:
    print("""
    1) Kilogram to Pound
    2) Pound to Kilogram
    """)
    choice_weight = int(input("Enter your choice :  "))

    if choice_weight == 1:
        val = float(input("Enter value in KG: "))
        print(kg_to_pound(val))

    elif choice_weight == 2:
        val = float(input("Enter value in Pound: "))
        print(pound_to_kg(val))

else:
    print("Error")


