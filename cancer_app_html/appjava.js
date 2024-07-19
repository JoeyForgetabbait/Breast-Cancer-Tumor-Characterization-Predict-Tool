<script>
    document.getElementById('executeButton').addEventListener('click', async () => {
        const texture = document.getElementById('texture').value;
        const symmetry = document.getElementById('symmetry).value;
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
                radius: radius,
                texture: texture,
                perimeter: perimeter,
                area: area,
                smoothness: smoothness,
                compactness: compactness,
                concavity: concavity,
                concave points: concave points,
                fractal dimension: fractal dimension
                // Include other input values here
            })
        });
        const data = await response.json();
        alert(data.result);
    });
</script>