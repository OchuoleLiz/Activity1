def convert_temperature(unit, temp):
    temp_convert_celsius = ((int(temp) - 32) * 5 / 9)
    temp_convert_fahrenheit = ((int(temp) * 1.8) + 32)

    if unit == "C" and (int(temp) >= 0 or int(temp) <= 0):
        print("Converting to Fahrenheit...")
        print("The temperature in Celsius is " + str(temp) + " and the temperature in Fahrenheit is " + str(
            temp_convert_fahrenheit) + ".")
    elif unit == "F" and (int(temp) >= 0 or int(temp) <= 0):
        print("Converting to Celsius...")
        print("The temperature in fahrenheit is " + str(temp) + " and the temperature in Celsius is " + str(
            temp_convert_celsius) + ".")
    else:
        print("Invalid Unit")

while True:
    unit = str(input("Input Degree in c or f \n")).capitalize()
    if unit == "C":
        print("Unit is Celsius.")
        break;
    elif unit == "F":
        print("Unit is Fahrenheit.")
        break;
    else:
        print("Invalid Unit.\nEnter either 'c' for Celsius or 'f' for Fahrenheit")


while True:
    temp = input("Input the Temperature...\n")
    try:
        val = int(temp)
        print("Input number is: ", val)
        break;
    except ValueError:
        print("This is not a Integer.\nPlease enter a valid Number")
convert_temperature(unit, temp)
