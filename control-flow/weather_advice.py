# weather_advice.py
#User input
weather_input = input(" What's the weather like today? (sunny/rainy/cold):"
#Provide Clothing Recommendations based on user input
    if weather_input == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather_input == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather_input == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("orry, I don't have recommendations for this weather.")
