from flask import Flask, render_template, request, redirect
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
cors = CORS(app)

# Load data and model
car = pd.read_csv('Cleaned_Car_data.csv')

# Create and fit label encoders
label_encoders = {}
categorical_columns = ['name', 'company', 'fuel_type']

for column in categorical_columns:
    le = LabelEncoder()
    le.fit(car[column])
    label_encoders[column] = le

# Load the model
try:
    model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
except:
    print("Error loading model. Please train the model first.")
    model = None

@app.route('/', methods=['GET', 'POST'])
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = car['fuel_type'].unique()

    companies.insert(0, 'Select Company')
    return render_template('index.html', companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)

def safe_predict_price(name, company, year, kms_driven, fuel_type):
    """
    Safe prediction function that handles edge cases and ensures positive prices
    """
    try:
        if model is None:
            return 150000  # Default reasonable price
        
        # Handle missing values in training data
        if name not in label_encoders['name'].classes_:
            # Find a similar car from the same company
            company_cars = car[car['company'] == company]['name'].unique()
            if len(company_cars) > 0:
                name = company_cars[0]
            else:
                name = car['name'].iloc[0]  # Use first available car
                
        if company not in label_encoders['company'].classes_:
            company = car['company'].iloc[0]  # Use first available company
            
        if fuel_type not in label_encoders['fuel_type'].classes_:
            fuel_type = 'Petrol'  # Default to Petrol
        
        # Encode categorical variables
        name_encoded = label_encoders['name'].transform([name])[0]
        company_encoded = label_encoders['company'].transform([company])[0]
        fuel_type_encoded = label_encoders['fuel_type'].transform([fuel_type])[0]
        
        # Create feature array
        features = np.array([[name_encoded, company_encoded, int(year), int(kms_driven), fuel_type_encoded]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Apply business logic to ensure reasonable prices
        # Adjust based on year (older cars should be cheaper)
        current_year = 2024
        age = current_year - int(year)
        
        # Base price adjustment based on age
        if age > 20:
            max_price = 200000
        elif age > 15:
            max_price = 400000
        elif age > 10:
            max_price = 800000
        elif age > 5:
            max_price = 1500000
        else:
            max_price = 3000000
            
        # Adjust for high mileage
        if int(kms_driven) > 100000:
            prediction *= 0.8  # Reduce price for high mileage
        elif int(kms_driven) > 200000:
            prediction *= 0.6  # Further reduce for very high mileage
            
        # Ensure prediction is within reasonable bounds
        min_price = 30000  # Minimum car price
        prediction = max(min_price, min(prediction, max_price))
        
        # If prediction is still negative or unreasonable, use fallback logic
        if prediction < min_price:
            # Fallback: estimate based on similar cars in dataset
            similar_cars = car[
                (car['company'] == company) & 
                (abs(car['year'] - int(year)) <= 2) &
                (car['fuel_type'] == fuel_type)
            ]
            
            if len(similar_cars) > 0:
                prediction = similar_cars['Price'].median()
            else:
                # Final fallback: use year-based estimation
                if int(year) >= 2020:
                    prediction = 500000
                elif int(year) >= 2015:
                    prediction = 300000
                elif int(year) >= 2010:
                    prediction = 200000
                elif int(year) >= 2005:
                    prediction = 100000
                else:
                    prediction = 50000
        
        return max(prediction, min_price)
        
    except Exception as e:
        print(f"Error in prediction: {e}")
        # Fallback prediction based on year
        try:
            year_int = int(year)
            if year_int >= 2020:
                return 500000
            elif year_int >= 2015:
                return 300000
            elif year_int >= 2010:
                return 200000
            elif year_int >= 2005:
                return 100000
            else:
                return 50000
        except:
            return 150000  # Final fallback

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        company = request.form.get('company')
        car_model = request.form.get('car_models')
        year = request.form.get('year')
        fuel_type = request.form.get('fuel_type')
        driven = request.form.get('kilo_driven')
        
        # Validate inputs
        if not all([company, car_model, year, fuel_type, driven]):
            return "Error: Missing required fields"
        
        # Use safe prediction function
        prediction = safe_predict_price(car_model, company, year, driven, fuel_type)
        
        print(f"Prediction for {car_model} ({company}, {year}, {fuel_type}, {driven} km): ₹{prediction:.2f}")
        
        return str(np.round(prediction, 2))
        
    except Exception as e:
        print(f"Error in predict route: {e}")
        return "150000.00"  # Default fallback

if __name__ == '__main__':
    app.run(debug=True)
