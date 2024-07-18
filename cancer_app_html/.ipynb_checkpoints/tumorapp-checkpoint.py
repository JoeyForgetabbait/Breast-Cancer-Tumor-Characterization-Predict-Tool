from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/runprediction', methods=['POST'])
def run_prediction():
    input_data = request.json

    # Extract input values from the request
    radius_mean = input_data.get('radius_mean')
    # Extract other input values here

    # Perform tumor prediction based on the input data
    result = "Benign" if float(radius_mean) < 15 else "Malignant"

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()
