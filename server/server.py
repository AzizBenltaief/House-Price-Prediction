import os

from flask import Flask, request, jsonify, render_template
import util
app = Flask(__name__)
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()

    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = float(request.form['bhk'])
        bath = float(request.form['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    except Exception as e:
        print("Error in /predict_home_price:", e)
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    import util
    util.load_saved_artifacts()  # Charge modèle + colonnes avant de lancer Flask
    print("Starting Python Flask Server for Home Price Prediction...")
    app.run(debug=True)

