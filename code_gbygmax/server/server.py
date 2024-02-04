from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    strain = float(request.form['strain'])
    location = request.form['location']
    RD= float(request.form['RD'])
    conf_pressure = float(request.form['conf_pressure'])

    response = jsonify({
        'prediction': util.get_prediction(strain, RD, conf_pressure, location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server...")
    util.load_saved_artifacts()
    app.run()