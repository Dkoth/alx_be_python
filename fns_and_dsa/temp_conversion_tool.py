#Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
OFFSET = 32

def convert_to_celsius(fahrenheit):
    #Converts a Fahrenheit temperature to Celsius.
    celsius = (fahrenheit - OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    #Converts a Celsius temperature to Fahrenheit.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + OFFSET
    return fahrenheit

def get_user_input():
    """Prompts the user to enter a temperature and the unit (Celsius or Fahrenheit).Handles invalid input and raises errors."""
    try:
        temperature = float(input("Enter the temperature to convert: "))
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        return temperature, unit

def perform_conversion():
    #Performs the temperature conversion based on user input.
    try:
        temperature, unit = get_user_input()
        if unit == 'C':
            #Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            #Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    perform_conversion()
