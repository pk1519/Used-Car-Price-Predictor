# 🚗 Car Price Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A machine learning-powered web application that predicts used car prices based on various features like company, model, year, fuel type, and kilometers driven. Built with **Streamlit** for an interactive and user-friendly experience.

## 🌟 Features

- **🎯 Accurate Predictions**: ML-powered price estimation using Linear Regression
- **📱 Interactive Web Interface**: Modern, responsive Streamlit UI
- **📊 Market Insights**: View similar cars and price distributions
- **📈 Data Visualization**: Interactive charts and graphs using Plotly
- **🔍 Smart Filtering**: Dynamic car model filtering based on company selection
- **⚡ Real-time Results**: Instant price predictions with validation
- **🛡️ Error Handling**: Robust handling of edge cases and missing data
- **📱 Mobile Friendly**: Responsive design that works on all devices

## 🎥 Demo

![Car Price Predictor Demo](https://via.placeholder.com/800x400/1f77b4/ffffff?text=Car+Price+Predictor+Demo)

*Live Demo: [Your App URL Here]*

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Model](#-model)
- [Deployment](#-deployment)
- [API Reference](#-api-reference)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/car-price-predictor.git
   cd car-price-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, navigate to the URL manually

### Alternative Installation Methods

<details>
<summary>Using Virtual Environment (Recommended)</summary>

```bash
# Create virtual environment
python -m venv car_predictor_env

# Activate virtual environment
# On Windows:
car_predictor_env\Scripts\activate
# On macOS/Linux:
source car_predictor_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```
</details>

<details>
<summary>Using Conda</summary>

```bash
# Create conda environment
conda create -n car_predictor python=3.9

# Activate environment
conda activate car_predictor

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```
</details>

## 💻 Usage

### Basic Usage

1. **Select Car Details**:
   - Choose the car company from the dropdown
   - Select the specific model (filtered by company)
   - Pick the year of purchase
   - Choose fuel type (Petrol/Diesel/CNG)
   - Enter kilometers driven

2. **Get Prediction**:
   - Click "🔮 Predict Price" button
   - View the estimated price with confidence range
   - Explore market insights and similar cars

### Advanced Features

- **Market Analysis**: View price distributions for similar cars
- **Data Exploration**: Examine the underlying dataset
- **Interactive Charts**: Hover over charts for detailed information
- **Price Range**: Get estimated price ranges with confidence intervals

## 📁 Project Structure

```
car-price-predictor/
├── 📄 streamlit_app.py          # Main Streamlit application
├── 📄 requirements.txt          # Python dependencies
├── 📄 Cleaned_Car_data.csv      # Cleaned dataset
├── 📄 LinearRegressionModel.pkl # Trained ML model
├── 📄 train_model_fixed.py      # Model training script
├── 📄 application_fixed.py      # Flask version (alternative)
├── 📄 quikr_predictor_fixed.py  # Data cleaning script
├── 📄 deploy.py                 # Local deployment helper
├── 📄 README.md                 # Project documentation
├── 📄 DEPLOYMENT_GUIDE.md       # Detailed deployment guide
├── 📄 requirements.txt          # Dependencies
└── 📁 static/                   # Static files (if any)
    └── 📁 templates/            # HTML templates (Flask version)
```

## 📊 Dataset

### Overview
- **Source**: Quikr Car Sales Data
- **Size**: 816 records after cleaning
- **Features**: 6 columns (name, company, year, price, kms_driven, fuel_type)
- **Target**: Car Price (in INR)

### Data Statistics
- **Companies**: 30+ car manufacturers
- **Models**: 200+ car models
- **Year Range**: 1995-2019
- **Price Range**: ₹30,000 - ₹60,00,000
- **Fuel Types**: Petrol, Diesel, CNG

### Data Preprocessing
- ✅ Removed non-numeric year values
- ✅ Cleaned price formatting (removed commas, "Ask For Price")
- ✅ Standardized kilometers driven format
- ✅ Handled missing fuel type values
- ✅ Simplified car names (first 3 words)
- ✅ Removed price outliers (>₹60 lakhs)

## 🤖 Model

### Algorithm
- **Primary Model**: Linear Regression
- **Preprocessing**: Label Encoding for categorical variables
- **Features**: Company, Model, Year, Kilometers Driven, Fuel Type
- **Target**: Price (INR)

### Model Performance
- **R² Score**: ~0.85 (85% variance explained)
- **Mean Absolute Error**: ~₹50,000
- **Training Data**: 80% of dataset
- **Test Data**: 20% of dataset

### Model Features
- **Robust Predictions**: Handles unseen car combinations
- **Price Validation**: Ensures realistic price ranges
- **Fallback Logic**: Uses similar cars for edge cases
- **Age Adjustment**: Considers car age in pricing

## 🌐 Deployment

### Streamlit Cloud (Recommended - FREE)

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Select `streamlit_app.py` as main file
   - Click "Deploy!"

### Other Deployment Options

<details>
<summary>Heroku Deployment</summary>

```bash
# Create Procfile
echo "web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy to Heroku
heroku create your-app-name
git push heroku main
```
</details>

<details>
<summary>Railway Deployment</summary>

1. Connect GitHub repo to [Railway](https://railway.app)
2. Railway auto-detects Streamlit apps
3. Your app will be live in minutes!
</details>

<details>
<summary>Render Deployment (Blueprint)</summary>

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/pk1519/Used-Car-Price-Predictor)

- This repository includes a `render.yaml` at the root with `rootDir: "Car price predictor pk"`.
- Click the button above or on Render choose "New → Blueprint" and select this repo.
- Build command: `pip install --upgrade pip && pip install -r requirements.txt`
- Start command: `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
- Environment variable: `PYTHON_VERSION=3.11.9` (set in `render.yaml`).
- Requirements file location: `Car price predictor pk/requirements.txt`.
  The `rootDir` ensures the build runs in this subfolder so `pip install -r requirements.txt` works.
</details>

## 🔧 API Reference

### Prediction Function

```python
def safe_predict_price(model, label_encoders, car_data, name, company, year, kms_driven, fuel_type):
    """
    Predict car price with validation and error handling
    
    Parameters:
    -----------
    model : sklearn.linear_model.LinearRegression
        Trained linear regression model
    label_encoders : dict
        Dictionary of label encoders for categorical variables
    car_data : pandas.DataFrame
        Original car dataset for fallback logic
    name : str
        Car model name
    company : str
        Car manufacturer
    year : int
        Year of manufacture
    kms_driven : int
        Kilometers driven
    fuel_type : str
        Type of fuel (Petrol/Diesel/CNG)
    
    Returns:
    --------
    float
        Predicted price in INR
    """
```

### Data Loading Functions

```python
@st.cache_data
def load_data():
    """Load and cache the car dataset"""
    
@st.cache_resource
def load_model_and_encoders():
    """Load and cache the ML model and encoders"""
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute
- 🐛 Report bugs
- 💡 Suggest new features
- 📝 Improve documentation
- 🔧 Submit pull requests

### Development Setup

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
6. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

### Code Style
- Follow PEP 8 guidelines
- Add docstrings to functions
- Include type hints where possible
- Write meaningful commit messages

## 🐛 Troubleshooting

### Common Issues

<details>
<summary>ModuleNotFoundError</summary>

**Problem**: Missing required packages

**Solution**:
```bash
pip install --upgrade streamlit pandas numpy scikit-learn plotly
```
</details>

<details>
<summary>FileNotFoundError</summary>

**Problem**: Missing data or model files

**Solution**: Ensure these files are in the same directory:
- `Cleaned_Car_data.csv`
- `LinearRegressionModel.pkl`
</details>

<details>
<summary>Port Already in Use</summary>

**Problem**: Port 8501 is occupied

**Solution**:
```bash
streamlit run streamlit_app.py --server.port 8502
```
</details>

## 📈 Future Enhancements

- [ ] **Advanced Models**: Implement Random Forest, XGBoost
- [ ] **More Features**: Add car condition, location, seller type
- [ ] **Image Recognition**: Predict price from car images
- [ ] **Market Trends**: Historical price trend analysis
- [ ] **Comparison Tool**: Compare multiple cars side-by-side
- [ ] **API Endpoint**: RESTful API for external integrations
- [ ] **Mobile App**: React Native mobile application
- [ ] **Real-time Data**: Integration with live car listing APIs

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Model Accuracy** | 85% |
| **Response Time** | <2 seconds |
| **Data Points** | 816 cars |
| **Supported Brands** | 30+ |
| **Supported Models** | 200+ |

## 🏆 Achievements

- ✅ **Negative Price Issue Fixed**: Robust validation ensures positive predictions
- ✅ **Interactive UI**: Modern Streamlit interface with real-time updates
- ✅ **Market Insights**: Advanced analytics and visualizations
- ✅ **Mobile Responsive**: Works seamlessly on all devices
- ✅ **Error Handling**: Graceful handling of edge cases
- ✅ **Easy Deployment**: Multiple deployment options available

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Car Price Predictor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- **Dataset**: Quikr Car Sales Data
- **Framework**: Streamlit for the amazing web app framework
- **ML Library**: Scikit-learn for machine learning capabilities
- **Visualization**: Plotly for interactive charts
- **Deployment**: Streamlit Cloud for free hosting

## 📞 Support

If you encounter any issues or have questions:

1. **Check the [Issues](https://github.com/yourusername/car-price-predictor/issues)** page
2. **Read the [Deployment Guide](DEPLOYMENT_GUIDE.md)**
3. **Join our [Discussions](https://github.com/yourusername/car-price-predictor/discussions)**
4. **Contact us** via email

## ⭐ Show Your Support

If this project helped you, please consider:
- ⭐ **Starring** the repository
- 🍴 **Forking** for your own use
- 📢 **Sharing** with others
- 🐛 **Reporting** bugs
- 💡 **Suggesting** improvements

---
## Screenshot


<img width="1919" height="729" alt="image" src="https://github.com/user-attachments/assets/99d10773-044f-4a7e-b769-524c8259971c" />
<img width="1546" height="628" alt="image" src="https://github.com/user-attachments/assets/898d11ee-2622-4ba4-bcd3-c7f0e4a4a17b" />
<img width="1472" height="836" alt="image" src="https://github.com/user-attachments/assets/51dc7eb5-b3ea-4c6e-991a-d401fd65be01" />
<img width="1919" height="828" alt="image" src="https://github.com/user-attachments/assets/a8253140-b4b4-4be8-b21e-e5a3e9c32dd7" />



<div align="center">

**🚗 Happy Car Price Predicting! 💰**

Made with ❤️ by [Your Name]

[⬆ Back to Top](#-car-price-predictor)

</div>
