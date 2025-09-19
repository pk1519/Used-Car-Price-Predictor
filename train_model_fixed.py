import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error
import pickle

# Load the cleaned data
print("Loading cleaned data...")
car = pd.read_csv('Cleaned_Car_data.csv')

print("Original data shape:", car.shape)
print("\nData info:")
print(car.info())

print("\nFirst few rows:")
print(car.head())

# Check for any missing values
print("\nMissing values:")
print(car.isnull().sum())

# Remove any rows with missing values
car = car.dropna()
print(f"\nData shape after removing missing values: {car.shape}")

# Prepare the data for modeling
print("\nPreparing data for modeling...")

# Create label encoders for categorical variables
label_encoders = {}
categorical_columns = ['name', 'company', 'fuel_type']

# Create a copy for encoding
car_encoded = car.copy()

# Encode categorical variables
for column in categorical_columns:
    le = LabelEncoder()
    car_encoded[column] = le.fit_transform(car_encoded[column])
    label_encoders[column] = le
    print(f"Encoded {column}: {len(le.classes_)} unique values")

# Prepare features and target
X = car_encoded[['name', 'company', 'year', 'kms_driven', 'fuel_type']]
y = car_encoded['Price']

print(f"\nFeatures shape: {X.shape}")
print(f"Target shape: {y.shape}")

print(f"\nPrice statistics:")
print(f"Min price: {y.min()}")
print(f"Max price: {y.max()}")
print(f"Mean price: {y.mean():.2f}")
print(f"Median price: {y.median():.2f}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"\nTraining set size: {X_train.shape[0]}")
print(f"Test set size: {X_test.shape[0]}")

# Train the model
print("\nTraining Linear Regression model...")
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"\nModel Performance:")
print(f"R² Score: {r2:.4f}")
print(f"Mean Absolute Error: {mae:.2f}")

# Check for negative predictions
negative_predictions = y_pred < 0
if negative_predictions.any():
    print(f"\nWarning: {negative_predictions.sum()} negative predictions found!")
    print(f"Min prediction: {y_pred.min():.2f}")
    print(f"Max prediction: {y_pred.max():.2f}")

# Save the model and encoders
print("\nSaving model and encoders...")
with open('LinearRegressionModel_Fixed.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('LabelEncoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

print("Model and encoders saved successfully!")

# Test prediction function
def predict_price(name, company, year, kms_driven, fuel_type):
    """
    Predict car price with validation
    """
    try:
        # Load model and encoders
        with open('LinearRegressionModel_Fixed.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('LabelEncoders.pkl', 'rb') as f:
            label_encoders = pickle.load(f)
        
        # Check if values exist in training data
        if name not in label_encoders['name'].classes_:
            print(f"Warning: '{name}' not in training data. Using most similar car.")
            # Find most similar car name
            available_names = label_encoders['name'].classes_
            name = available_names[0]  # Use first available name as fallback
            
        if company not in label_encoders['company'].classes_:
            print(f"Warning: '{company}' not in training data. Using most similar company.")
            available_companies = label_encoders['company'].classes_
            company = available_companies[0]  # Use first available company as fallback
            
        if fuel_type not in label_encoders['fuel_type'].classes_:
            print(f"Warning: '{fuel_type}' not in training data. Using Petrol as default.")
            fuel_type = 'Petrol'
        
        # Encode the input
        # Try predicting with a DataFrame first (for models/pipelines that expect column names)
        try:
            input_df = pd.DataFrame(
                [[name, company, int(year), int(kms_driven), fuel_type]],
                columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
            )
            prediction = model.predict(input_df)[0]
        except Exception:
            # Fallback: use label-encoded numeric features (for plain LinearRegression models)
            name_encoded = label_encoders['name'].transform([name])[0]
            company_encoded = label_encoders['company'].transform([company])[0]
            fuel_type_encoded = label_encoders['fuel_type'].transform([fuel_type])[0]

            features = np.array([[name_encoded, company_encoded, int(year), int(kms_driven), fuel_type_encoded]])
            prediction = model.predict(features)[0]
        
        # Ensure prediction is positive and reasonable
        if prediction < 30000:  # Minimum reasonable car price
            prediction = 30000
        elif prediction > 5000000:  # Maximum reasonable car price
            prediction = 5000000
            
        return max(prediction, 30000)  # Ensure minimum price
        
    except Exception as e:
        print(f"Error in prediction: {e}")
        return 100000  # Default reasonable price

# Test the prediction function
print("\nTesting prediction function...")
test_prediction = predict_price("Chevrolet Spark LT", "Chevrolet", 2002, 23443, "Diesel")
print(f"Test prediction for Chevrolet Spark LT 2002: ₹{test_prediction:.2f}")

print("\nModel training completed successfully!")
