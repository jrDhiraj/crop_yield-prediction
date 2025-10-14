from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load your saved model and preprocessor
model = pickle.load(open(r'model\model_dt.pkl', 'rb'))
preprocessor = pickle.load(open(r'model\preprocessor (2).pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        Area = request.form['Area']
        Item = request.form['Item']
        Year = int(request.form['Year'])
        average_rain_fall_mm_per_year = float(request.form['average_rain_fall_mm_per_year'])
        pesticides_tonnes = float(request.form['pesticides_tonnes'])
        avg_temp = float(request.form['avg_temp'])

        # Prepare feature array
        features = np.array([[Area, Item, Year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp]])

        # Transform and predict
        transformed_features = preprocessor.transform(features)
        prediction = model.predict(transformed_features)

        result = round(prediction[0], 2)
        return render_template('index.html', prediction_text=f'Predicted Yield: {result} hg/ha')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
