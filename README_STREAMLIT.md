# 🚗 Car Price Predictor - Streamlit App

A machine learning-powered web application to predict used car prices based on various features like company, model, year, fuel type, and kilometers driven.

## 🌟 Features

- **Interactive Web Interface**: User-friendly Streamlit interface
- **Real-time Predictions**: Instant price predictions using machine learning
- **Market Insights**: View similar cars and price distributions
- **Data Visualization**: Interactive charts and graphs
- **Responsive Design**: Works on desktop and mobile devices

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Local Installation & Setup

### 1. Clone or Download the Project
```bash
git clone <your-repo-url>
cd Used-Car-Price-Predictor/Car\ price\ predictor\ pk/
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run streamlit_app.py
```

The app will open in your default web browser at `http://localhost:8501`

## 🌐 Deploy to Streamlit Cloud (Free)

### Method 1: Direct Upload to Streamlit Cloud

1. **Create a GitHub Repository**
   - Create a new repository on GitHub
   - Upload all your project files including:
     - `streamlit_app.py`
     - `requirements.txt`
     - `Cleaned_Car_data.csv`
     - `LinearRegressionModel.pkl`

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub account
   - Select your repository
   - Set main file path: `streamlit_app.py`
   - Click "Deploy!"

### Method 2: Using Streamlit Community Cloud

1. **Prepare Your Repository**
   ```
   your-repo/
   ├── streamlit_app.py
   ├── requirements.txt
   ├── Cleaned_Car_data.csv
   ├── LinearRegressionModel.pkl
   └── README.md
   ```

2. **Deploy Steps**
   - Visit [streamlit.io/cloud](https://streamlit.io/cloud)
   - Sign in with GitHub
   - Click "New app"
   - Choose your repository
   - Select branch (usually `main`)
   - Set main file: `streamlit_app.py`
   - Click "Deploy!"

## 🔧 Alternative Deployment Options

### 1. Heroku Deployment
```bash
# Install Heroku CLI
# Create Procfile
echo "web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy to Heroku
heroku create your-app-name
git push heroku main
```

### 2. Railway Deployment
- Connect your GitHub repo to [Railway](https://railway.app)
- Railway will automatically detect and deploy your Streamlit app

### 3. Render Deployment
- Connect your GitHub repo to [Render](https://render.com)
- Set build command: `pip install -r requirements.txt`
- Set start command: `streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`

## 📁 Required Files for Deployment

Make sure these files are in your project directory:

1. **streamlit_app.py** - Main Streamlit application
2. **requirements.txt** - Python dependencies
3. **Cleaned_Car_data.csv** - Cleaned dataset
4. **LinearRegressionModel.pkl** - Trained ML model
5. **README.md** - Project documentation

## 🛠️ Troubleshooting

### Common Issues:

1. **Module Not Found Error**
   ```bash
   pip install --upgrade streamlit pandas numpy scikit-learn plotly
   ```

2. **File Not Found Error**
   - Ensure `Cleaned_Car_data.csv` and `LinearRegressionModel.pkl` are in the same directory as `streamlit_app.py`

3. **Port Issues (Local)**
   ```bash
   streamlit run streamlit_app.py --server.port 8502
   ```

4. **Memory Issues on Free Hosting**
   - Consider using a smaller dataset or optimizing the model

## 📊 App Features

- **Car Selection**: Choose from available companies and models
- **Price Prediction**: Get instant price estimates
- **Market Analysis**: View similar cars and price trends
- **Interactive Charts**: Visualize price distributions
- **Responsive Design**: Works on all devices

## 🔄 Updating the App

To update your deployed app:
1. Make changes to your code
2. Push to GitHub
3. Streamlit Cloud will automatically redeploy

## 💡 Tips for Better Performance

1. **Optimize Data Loading**: Use `@st.cache_data` for data loading
2. **Model Caching**: Use `@st.cache_resource` for model loading
3. **Reduce File Sizes**: Compress large files if possible
4. **Error Handling**: Implement robust error handling

## 📞 Support

If you encounter any issues:
1. Check the Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
2. Visit Streamlit Community: [discuss.streamlit.io](https://discuss.streamlit.io)
3. Check GitHub issues in your repository

## 🎉 Success!

Once deployed, your app will be accessible via a public URL that you can share with anyone!

Example: `https://your-app-name.streamlit.app`

---

**Happy Predicting! 🚗💰**
