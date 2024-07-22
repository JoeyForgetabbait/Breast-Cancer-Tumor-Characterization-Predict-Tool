from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import joblib


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['Breast_Cancer_Tumor_Metrics']
collection = db['Metrics_Table']

# Load the pre-trained model from the .pkl file
model = joblib.load('SVM_Model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/runprediction', methods=['GET', 'POST'])
def run_prediction():
    if request.method == 'GET':
        # Handle GET request to fetch data from MongoDB
        data_from_db = collection.find()
        response_data = []
        for item in data_from_db:
            response_data.append({
                'radius': item['radius'],
                'texture': item['texture'],
                'perimeter': item['perimeter'],
                'area': item['area'],
                'smoothness': item['smoothness'],
                'compactness': item['compactness'],
                'concavity': item['concavity'],
                'concave_points': item['concave_points'],
                'symmetry': item['symmetry'],
                'fractal_dimension': item['fractal_dimension'],
                'result': item['result']
            })
        
        return jsonify({'data': response_data})
    
    elif request.method == 'POST':
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

        # Update the MongoDB document with the input data and prediction result
        data = {
            'radius': radius,
            'texture': texture,
            'perimeter': perimeter,
            'area': area,
            'smoothness': smoothness,
            'compactness': compactness,
            'concavity': concavity,
            'concave_points': concave_points,
            'symmetry': symmetry,
            'fractal_dimension': fractal_dimension,
            'result': result[0]
        }
        collection.insert_one(data)

        return jsonify({'result': result[0]})

if __name__ == '__main__':
    app.run()
    
    
    
# def run_prediction(request):
#     # Example input that might cause the error
#     potential_none_value = None

#     try:
#         # Attempt to convert the value to float
#         float_value = float(potential_none_value)
#     except TypeError:
#         # Handle the case where the conversion fails due to NoneType
#         print("Error: Cannot convert None to float")
#         return HttpResponse(status=400)

#     # Continue processing with the safe float value
#     # ...