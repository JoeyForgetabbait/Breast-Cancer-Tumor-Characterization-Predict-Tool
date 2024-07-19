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
    radius = float(input_data.get('radius'))
    texture = float(input_data.get('texture'))
    perimeter = float(input_data.get('perimeter'))
    area = float(input_data.get('area'))
    smoothness = float(input_data.get('smoothness'))
    compactness = float(input_data.get('compactness'))
    concavity = float(input_data.get('concavity'))
    concave_points = float(input_data.get('concave_points'))
    symmetry = float(input_data.get('symmetry'))
    fractal_dimension = float(input_data.get('fractal_dimension'))

    # Make predictions using the loaded model
    result = model.predict([[radius, texture, perimeter, area, smoothness, compactness, concavity, concave_points, symmetry, fractal_dimension]])

    # Return the prediction result
    return jsonify({'result': result[0]})

if __name__ == '__main__':
    app.run()