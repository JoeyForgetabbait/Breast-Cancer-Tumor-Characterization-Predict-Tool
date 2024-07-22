#write d3 function to read from api route - mongo db 
#add html components to div tag
<script>
    document.getElementById('executeButton').addEventListener('click', async () => {
        const texture = document.getElementById('texture').value;
        const symmetry = document.getElementById('symmetry').value;
        const perimeter = document.getElementById('perimeter').value;
        const radius = document.getElementById('radius').value;
        const area = document.getElementById('area').value;
        const smoothness = document.getElementById('smoothness').value;
        const compactness = document.getElementById('compactness').value;
        const concavity = document.getElementById('concavity').value;
        const concave_points = document.getElementById('concave_points').value;
        const fractal_dimension = document.getElementById('fractal_dimension').value;

        const inputData = {
            radius: parseFloat(radius),
            symmetry: parseFloat(symmetry),
            texture: parseFloat(texture),
            perimeter: parseFloat(perimeter),
            area: parseFloat(area),
            smoothness: parseFloat(smoothness),
            compactness: parseFloat(compactness),
            concavity: parseFloat(concavity),
            concave_points: parseFloat(concave_points),
            fractal_dimension: parseFloat(fractal_dimension)
            // Include other input values here
        };

        // Push input data to MongoDB
        fetch('/pushdata', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(inputData)
        })
        .then(response => {
            if (response.ok) {
                console.log('Input data pushed to MongoDB successfully');

                // Retrieve prediction data from MongoDB
                fetch('/getprediction', {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(predictionResponse => predictionResponse.json())
                .then(predictionData => {
                    console.log('Prediction data retrieved from MongoDB:', predictionData);
                    // Handle the prediction data as needed
                })
                .catch(error => {
                    console.error('Error retrieving prediction data from MongoDB:', error);
                });
            } else {
                console.error('Failed to push input data to MongoDB');
            }
        })
        .catch(error => {
            console.error('Error pushing input data to MongoDB:', error);
        });
    });
</script>