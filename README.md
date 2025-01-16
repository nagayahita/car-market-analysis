# Car Market Analysis

Advanced car market analysis tool for predicting car prices and providing market insights.

## Features
- 📊 Comprehensive data preprocessing
- 💹 Interactive market analysis
- 📈 Price trend visualizations
- 🎯 Smart price recommendations

## 🚀 Getting Started

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/car-market-analysis.git
cd car-market-analysis

# Install dependencies
pip install -r requirements.txt

# Import required modules
from src.analyzer import CarMarketAnalyzer
import pandas as pd

# Load your data
data = pd.read_csv('data/train.csv')

# Initialize analyzer
analyzer = CarMarketAnalyzer(data)

# Get market insights
market_overview = analyzer.create_market_overview()

# Get recommendations
recommendations = analyzer.generate_price_recommendations(
    budget=50000,
    category="Luxury"
)
