import requests

api_key = "cc637fa8ebea451911232cf9c2d940b0"

while True:
    try:
        city = input("Enter the City name: ").strip()

        if city.lower() == "stop":
            print("Thank You!")
            break

        if city == "":
            raise ValueError("Error, City is Empty!")

        if city.isdigit():
            raise ValueError("Error, Invalid City Name!")

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        data = response.json()

        if str(data["cod"]) != "200":
            raise ValueError("City not found. Enter a valid city name!")

        
        print("============== Weather Details ==============")
        print(f"City : {data['name']}")
        print(f"Temperature : {data['main']['temp']}°C")
        print(f"Humidity : {data['main']['humidity']}%")
        print(f"Weather : {data['weather'][0]['description']}")
        print(f"Wind Speed : {data['wind']['speed']} m/s")
        print("==============================================")

    except ValueError as v:
        print(v)