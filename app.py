from flask import Flask, render_template
import openrouteservice

app = Flask(__name__)

# OpenRouteService API Key (already yours)
ORS_API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6Ijc5ZWI2ZDlkOGE3YjRkMDBiYWFhZjZkMzAyZmVlNGU4IiwiaCI6Im11cm11cjY0In0="


@app.route('/')
def index():
    return render_template('index.html')  # ✅ Home page

@app.route('/about')
def about():
    return render_template('about.html')  # ✅ This must be 'about.html'

@app.route('/route1')
def route1():
    start = [77.2167, 28.6315]   # Connaught Place
    end = [77.2295, 28.6129]     # India Gate

    client = openrouteservice.Client(key=ORS_API_KEY)
    route = client.directions((start, end), profile='driving-car', format='geojson')
    coordinates = route['features'][0]['geometry']['coordinates']

    return render_template('routing.html', coords=coordinates)

if __name__ == '__main__':
    app.run(debug=True)