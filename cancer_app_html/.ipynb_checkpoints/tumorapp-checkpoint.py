from flask import Flask, render_template, jsonify, request
import joblib

app = Flask(__name__)

# Load the pre-trained model from the .pkl file
model = joblib.load('SVM_Model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/runprediction', methods=['POST'])
def run_prediction():
    input_data = request.form

    # Extract input values from the request
    radius = input_data.get('radius')
    texture = input_data.get('texture')
    perimeter = input_data.get('perimeter')
    area = input_data.get('area')
    smoothness = input_data.get('smoothness')
    compactness = input_data.get('compactness')
    concavity = input_data.get('concavity')
    concave_points = input_data.get('concave points')
    symmetry = input_data.get('symmetry')
    fractal_dimension = input_data.get('fractal dimension')

    # Make predictions using the loaded model
    result = model.predict([[radius, texture, perimeter, area, smoothness, compactness, concavity, concave_points, symmetry, fractal_dimension]])

    # Return the prediction result
    return jsonify({'result': result[0]})

if __name__ == '__main__':
    app.run()