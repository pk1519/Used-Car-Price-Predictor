#!/usr/bin/env python3
"""
Deployment helper script for Car Price Predictor Streamlit App
"""

import os
import subprocess
import sys

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        'streamlit_app.py',
        'requirements.txt',
        'Cleaned_Car_data.csv',
        'LinearRegressionModel.pkl'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    print("✅ All required files found!")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies!")
        return False

def run_streamlit():
    """Run the Streamlit app"""
    print("🚀 Starting Streamlit app...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])
    except KeyboardInterrupt:
        print("\n👋 Streamlit app stopped!")
    except Exception as e:
        print(f"❌ Error running Streamlit: {e}")

def main():
    print("🚗 Car Price Predictor - Deployment Helper")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Please ensure all required files are present before deploying.")
        return
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Failed to install dependencies. Please check your Python environment.")
        return
    
    # Run Streamlit
    print("\n🎉 Everything is ready!")
    print("📱 Your app will open in your default browser.")
    print("🔗 Local URL: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the app")
    print("-" * 50)
    
    run_streamlit()

if __name__ == "__main__":
    main()
