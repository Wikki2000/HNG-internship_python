from flask import Flask, request, jsonify, render_template
import requests
from os import environ

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/hello')
def hello():
    """
    Handle GET requests to the '/api/hello' endpoint.
    Returns a JSON response with a greeting message and client information.
    """
    visitor_name = request.args.get("visitor_name", "visitor")

    # Obtain the client's IP address from the request.
    client_ip = request.remote_addr

    # Mock IP for test and development purposes.
    # For production, remove or comment out the following line.
    # client_ip = "8.8.8.8"

    # Get geolocation and other data based on the client IP address.
    location_data = requests.get(f'http://ip-api.com/json/{client_ip}').json()
    city = location_data.get("city", "unknown")
    lat = location_data.get('lat')
    lon = location_data.get('lon')

    # Initialize temperature to 'Unknown'
    temperature = 'Unknown'

    # Retrieve weather data based on latitude and longitude.
    if lat and lon:
        api_key = environ["API_KEY"]
        url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}'
        weather_response = requests.get(url)
        
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
            temperature = weather_data['current']['temp_c']
        else:
            # To handle case were weather api fails
            print(f"Failed to retrieve weather data: {weather_response.status_code}")

    # Construct the greeting message.
    greeting = f"Hello, {visitor_name}! The temperature is {temperature} degrees Celsius in {city}"

    # Prepare the JSON response.
    response = {
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

