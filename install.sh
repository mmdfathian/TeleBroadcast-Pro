#!/bin/bash

# TeleBroadcast-Pro Auto Installer
# --------------------------------

echo "🚀 Starting TeleBroadcast-Pro installation..."

# 1. Check for Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 could not be found. Please install it first."
    exit
fi

# 2. Create Virtual Environment
echo "📦 Creating virtual environment (venv)..."
python3 -m venv venv
source venv/bin/activate

# 3. Upgrade pip and install requirements
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Setup .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "🔑 Setting up your .env file..."
    read -p "Enter your API_ID: " api_id
    read -p "Enter your API_HASH: " api_hash
    echo "API_ID=$api_id" > .env
    echo "API_HASH=$api_hash" >> .env
    echo "✅ .env file created successfully."
else
    echo "ℹ️ .env file already exists. Skipping..."
fi

echo "-----------------------------------------------"
echo "🎉 Installation Complete!"
echo "👉 To run the app, use: source venv/bin/activate && python main.py"
echo "-----------------------------------------------"
