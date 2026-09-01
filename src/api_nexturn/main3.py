from flask import Flask, request,render_template
import requests
import json

app= Flask(__name__)

API="c31bfbffd4b586eebc731e1dee87c1e7"


CITIES = [
    {'name': 'Mumbai', 'lat': 19.0760, 'lon': 72.8777},
    {'name': 'Hyderabad', 'lat': 17.3850, 'lon': 78.4867},
    {'name': 'Prayagraj', 'lat': 25.4358, 'lon': 81.8463},
    {'name': 'Delhi', 'lat': 28.7041, 'lon': 77.1025},
    {'name': 'Bengaluru', 'lat': 12.9716, 'lon': 77.5946},
    {'name': 'Chennai', 'lat': 13.0827, 'lon': 80.2707},
    {'name': 'Kolkata', 'lat': 22.5726, 'lon': 88.3639}
]
# response= requests.json(URL)

@app.get("/")
def index():
   return render_template("index.html",city_list= CITIES)

@app.get("/<lat>/<lon>")

def handle_home(lat,lon):
 URL =f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}"

 response= requests.get(URL)
 data= response.json()
 city_name= data['name']
 temp= data['main']['temp']-273.15

 weather_tag=""

 if temp <30:
    weather_tag="cool"

 elif temp >30:
    weather_tag="warmer"
    
 elif temp <20:
    weather_tag="very cold"

 elif temp >40:
    weather_tag="hot"

 return render_template ('index.html',
                         city_list= CITIES
    # city= city_name,
    # temp= temp,
    # weather= weather_tag)
 )


@app.get("/")
def handle_city():
   URL =f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API}"

   response = requests.get(URL)
   data = response.json()



# @app.post()


# def post_data()


if __name__== "__main__":
    app.run(debug= True)