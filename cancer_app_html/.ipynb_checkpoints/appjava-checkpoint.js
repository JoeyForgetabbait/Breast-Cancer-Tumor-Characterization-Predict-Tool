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
        
        // Add similar lines for other input fields

        const response = await fetch('/runprediction', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
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
            })
        });

        if (response.ok) {
            const data = await response.json();
            alert(data.result);
        } else {
            alert('Failed to get prediction. Please try again.');
        }
    });
</script>