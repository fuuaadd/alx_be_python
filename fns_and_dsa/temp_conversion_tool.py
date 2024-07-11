
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 



def convert_to_celsius(fahrenheit):
    r = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return r
def convert_to_fahrenheit(celsius):
    r = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return r
def main():
    temperature_input = input("Enter the temperature to convert: ")
    if not temperature_input.replace('.', '', 1).isdigit() and not (temperature_input.startswith('-') and temperature_input[1:].replace('.', '', 1).isdigit()):
        print("Invalid temperature. Please enter a numeric value.")
        return
    temperature = float(temperature_input)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
