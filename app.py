from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/route', methods=["GET", "POST"])
def smart_route():
    if request.method == "POST":
        # Extract start and end from form (or use fixed ones for now)
        start = request.form.get('start') or "Connaught Place, Delhi"
        end = request.form.get('end') or "India Gate, Delhi"

        # For now, just mock coordinates (real code will use geocoder or hardcoded lat/lon)
        start_coords = (28.6315, 77.2167)
        end_coords = (28.6129, 77.2295)

        # Placeholder: pass these to frontend
        route_coords = [
            [77.2167, 28.6315],
            [77.2200, 28.6220],
            [77.2295, 28.6129]
        ]
        return render_template('routing.html', coords=route_coords)
    return render_template('routing.html')

if __name__ == '__main__':
    app.run(debug=True)
