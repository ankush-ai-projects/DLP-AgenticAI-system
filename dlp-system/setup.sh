#!/bin/bash
# Development setup script

echo "🚀 Setting up FastAPI DLP System..."

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create logs directory
mkdir -p logs

# Initialize database
echo "🗄️  Initializing database..."
python -c "from app.db.session import engine; from app.models.base import Base; Base.metadata.create_all(bind=engine)"

echo "✓ Setup complete!"
echo ""
echo "📖 Quick start:"
echo "  1. Activate venv: source venv/bin/activate"
echo "  2. Run app: uvicorn app.main:app --reload"
echo "  3. Open: http://localhost:8000/docs"
