#!/bin/bash

# --- Aurum-9 Framework Deployment Script ---
echo "🛡️ INITIALIZING AURUM-9: C3MRS FRAMEWORK..."
echo "------------------------------------------"

# 1. Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ ERROR: Python 3 is not installed. Please install it to proceed."
    exit 1
fi

# 2. Create Virtual Environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "[*] Creating isolated virtual environment..."
    python3 -m venv venv
fi

# 3. Activate environment and install requirements
echo "[*] Installing 'Iron-Clad' dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 4. Final System Check
echo "[+] Environment verified."
echo "[*] Launching Neural Commander..."
echo "------------------------------------------"

# 5. Launch the Framework
python3 main.py
