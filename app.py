from flask import Flask, jsonify
import network as n

app = Flask(__name__)

# Weather API details
api_key = "d3dda624a81af4587511e0524a1bbc5a"
lat = 12.5776539
lon = 106.9349172

@app.route('/weather')
def weather():
    forecast_data = n.get_weather_forecast(api_key, lat, lon)
    return jsonify(forecast_data)

if __name__ == "__main__":
    app.run(debug=True)

