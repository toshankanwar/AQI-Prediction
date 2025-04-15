from flask import Flask, request, jsonify
from flask_cors import CORS
from predictor import predict_aqi

app = Flask(__name__)
CORS(app)  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    city = data['city']
    date_str = data['date']
    
    try:
    
        prediction = predict_aqi(city, date_str)

        # Ensure the prediction is a native Python float (not float32)
        prediction = float(prediction)

        return jsonify({'predicted_aqi': prediction})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)