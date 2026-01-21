#!/bin/bash
# Setup script for Expense Tracker Application

echo "=========================================="
echo "Expense Tracker - Setup Script"
echo "=========================================="
echo ""

# Check Python version
echo "Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "✓ Python $PYTHON_VERSION found"
else
    echo "✗ Python 3 not found. Please install Python 3.10 or higher."
    exit 1
fi

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Removing broken virtual environment..."
    rm -rf venv
fi
python3 -m venv venv
echo "✓ Virtual environment created"

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1
echo "✓ Dependencies installed"

# Create data directory if needed
if [ ! -d "data" ]; then
    mkdir data
    echo "✓ Data directory created"
else
    echo "✓ Data directory exists"
fi

echo ""
echo "=========================================="
echo "Setup complete!"
echo "=========================================="
echo ""
echo "To run the application:"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
