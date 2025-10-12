FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

def main():
    temp =  float(input("Enter the temperature to convert: "))
    unit = (input ("Is this temperature in Celsius or Fahrenheit? (C/F): "))
    if unit == "C":
        result = convert_to_fahrenheit(temp)
        print (result)
    elif unit == "F":
        result = convert_to_celsius(temp)
        print (result)
    else:
        print ("Invalid temperature. Please enter a numeric value.")


if __name__ == "__main__":
    main()