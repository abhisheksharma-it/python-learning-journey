import requests
class WeatherApp:
    def __init__(self, city):
        self.city = city

    def show_weather(self):
        # wttr.in se clean text fetch karke direct print
        print(requests.get(f"https://wttr.in/{self.city}?format=%l:+%t,+%C").text)

# Object creation and method call in one line
WeatherApp(input("City: ")).show_weather()
