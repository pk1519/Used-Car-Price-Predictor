import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 20px 0;
    }
    .info-box {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and cache the car data"""
    try:
        car_data = pd.read_csv('Cleaned_Car_data.csv')
        return car_data
    except FileNotFoundError:
        st.error("❌ Cleaned_Car_data.csv not found! Please ensure the data file is in the same directory.")
        return None

@st.cache_resource
def load_model_and_encoders():
    """Load and cache the model and encoders"""
    try:
        # Try to load the model
        model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
        
        # Create label encoders from the data
        car_data = load_data()
        if car_data is not None:
            label_encoders = {}
            categorical_columns = ['name', 'company', 'fuel_type']
            
            for column in categorical_columns:
                le = LabelEncoder()
                le.fit(car_data[column])
                label_encoders[column] = le
            
            return model, label_encoders
        else:
            return None, None
            
    except FileNotFoundError:
        st.error("❌ Model file not found! Please ensure LinearRegressionModel.pkl is in the same directory.")
        return None, None

def safe_predict_price(model, label_encoders, car_data, name, company, year, kms_driven, fuel_type):
    """
    Safe prediction function that handles edge cases and ensures positive prices
    """
    try:
        if model is None or label_encoders is None:
            return 150000  # Default reasonable price
        
        # Handle missing values in training data
        if name not in label_encoders['name'].classes_:
            # Find a similar car from the same company
            company_cars = car_data[car_data['company'] == company]['name'].unique()
            if len(company_cars) > 0:
                name = company_cars[0]
                st.warning(f"⚠️ Exact model not found. Using similar model: {name}")
            else:
                name = car_data['name'].iloc[0]  # Use first available car
                st.warning(f"⚠️ Company not found in training data. Using: {name}")
                
        if company not in label_encoders['company'].classes_:
            company = car_data['company'].iloc[0]  # Use first available company
            st.warning(f"⚠️ Company not found. Using: {company}")
            
        if fuel_type not in label_encoders['fuel_type'].classes_:
            fuel_type = 'Petrol'  # Default to Petrol
            st.warning("⚠️ Fuel type not found. Using: Petrol")
        
        # Encode categorical variables
        name_encoded = label_encoders['name'].transform([name])[0]
        company_encoded = label_encoders['company'].transform([company])[0]
        fuel_type_encoded = label_encoders['fuel_type'].transform([fuel_type])[0]
        
        # Create feature array
        features = np.array([[name_encoded, company_encoded, int(year), int(kms_driven), fuel_type_encoded]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        
        # Apply business logic to ensure reasonable prices
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
            similar_cars = car_data[
                (car_data['company'] == company) & 
                (abs(car_data['year'] - int(year)) <= 2) &
                (car_data['fuel_type'] == fuel_type)
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
        st.error(f"❌ Error in prediction: {e}")
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

def main():
    # Header
    st.markdown('<h1 class="main-header">🚗 Car Price Predictor</h1>', unsafe_allow_html=True)
    st.markdown("### Predict the price of your car using machine learning!")
    
    # Load data and model
    car_data = load_data()
    model, label_encoders = load_model_and_encoders()
    
    if car_data is None:
        st.stop()
    
    # Sidebar for inputs
    st.sidebar.header("🔧 Car Details")
    st.sidebar.markdown("Fill in the details of your car:")
    
    # Input fields
    companies = sorted(car_data['company'].unique())
    selected_company = st.sidebar.selectbox("🏢 Select Company", companies)
    
    # Filter car models based on selected company
    company_cars = car_data[car_data['company'] == selected_company]['name'].unique()
    selected_model = st.sidebar.selectbox("🚙 Select Model", sorted(company_cars))
    
    # Year selection
    years = sorted(car_data['year'].unique(), reverse=True)
    selected_year = st.sidebar.selectbox("📅 Year of Purchase", years)
    
    # Fuel type
    fuel_types = car_data['fuel_type'].unique()
    selected_fuel = st.sidebar.selectbox("⛽ Fuel Type", fuel_types)
    
    # Kilometers driven
    kms_driven = st.sidebar.number_input(
        "🛣️ Kilometers Driven", 
        min_value=0, 
        max_value=500000, 
        value=50000, 
        step=1000,
        help="Enter the total kilometers the car has been driven"
    )
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 Car Information")
        
        # Display selected car info
        info_data = {
            "Company": selected_company,
            "Model": selected_model,
            "Year": selected_year,
            "Fuel Type": selected_fuel,
            "Kilometers Driven": f"{kms_driven:,} km"
        }
        
        for key, value in info_data.items():
            st.markdown(f"**{key}:** {value}")
        
        # Predict button
        if st.button("🔮 Predict Price", type="primary", use_container_width=True):
            with st.spinner("Calculating price..."):
                predicted_price = safe_predict_price(
                    model, label_encoders, car_data,
                    selected_model, selected_company, selected_year, 
                    kms_driven, selected_fuel
                )
                
                # Display prediction
                st.markdown(f"""
                <div class="prediction-box">
                    <h2 style="color: #1f77b4; margin: 0;">💰 Predicted Price</h2>
                    <h1 style="color: #2e8b57; margin: 10px 0;">₹{predicted_price:,.2f}</h1>
                    <p style="margin: 0; color: #666;">This is an estimated price based on similar cars in our database.</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Show price range
                lower_bound = predicted_price * 0.9
                upper_bound = predicted_price * 1.1
                st.info(f"💡 **Price Range:** ₹{lower_bound:,.2f} - ₹{upper_bound:,.2f}")
    
    with col2:
        st.subheader("📈 Market Insights")
        
        # Show similar cars
        similar_cars = car_data[
            (car_data['company'] == selected_company) & 
            (abs(car_data['year'] - selected_year) <= 2)
        ]
        
        if len(similar_cars) > 0:
            st.write(f"**Similar {selected_company} cars ({selected_year}±2 years):**")
            avg_price = similar_cars['Price'].mean()
            st.metric("Average Price", f"₹{avg_price:,.0f}")
            st.metric("Number of Similar Cars", len(similar_cars))
            
            # Price distribution chart
            if len(similar_cars) > 1:
                fig = px.histogram(
                    similar_cars, 
                    x='Price', 
                    title=f"{selected_company} Price Distribution",
                    nbins=10
                )
                fig.update_layout(height=300)
                st.plotly_chart(fig, use_container_width=True)
    
    # Additional insights
    st.subheader("📊 Dataset Overview")
    
    col3, col4, col5, col6 = st.columns(4)
    
    with col3:
        st.metric("Total Cars", len(car_data))
    
    with col4:
        st.metric("Companies", car_data['company'].nunique())
    
    with col5:
        st.metric("Models", car_data['name'].nunique())
    
    with col6:
        avg_price = car_data['Price'].mean()
        st.metric("Avg Price", f"₹{avg_price:,.0f}")
    
    # Show data sample
    with st.expander("🔍 View Sample Data"):
        st.dataframe(car_data.head(10))
    
    # Footer
    st.markdown("---")
    st.markdown(
        "**Note:** This prediction is based on historical data and market trends. "
        "Actual prices may vary based on car condition, location, and market demand."
    )

if __name__ == "__main__":
    main()
