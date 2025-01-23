# Car Market Analysis System

## Overview
Advanced system for analyzing car market data and providing price recommendations. Features data preprocessing, market analysis, and AI-powered price suggestions based on multiple factors.

## Features
- Robust data preprocessing and cleaning
- Comprehensive market insights
- Price recommendations based on multiple criteria
- Interactive visualizations
- Value score calculation

## Technical Details
- Data preprocessing with custom DataPreprocessor class
- Market analysis with CarMarketAnalyzer class
- Standardization of manufacturer names and fuel types
- Calculation of derived metrics (Vehicle Age, Price/Year, etc.)

## Key Metrics
- Price analysis (min, max, average, median)
- Manufacturer statistics
- Vehicle categories analysis 
- Custom value scoring system

## Visualization Features
- Price distribution histograms
- Price vs Production Year scatter plots
- Category-wise price distribution box plots
- Interactive Plotly visualizations

## Installation

pip install -r requirements.txt

# Initialize preprocessor and analyzer
preprocessor = DataPreprocessor()
processed_data = preprocessor.process_dataset(data)
analyzer = CarMarketAnalyzer(processed_data)

# Get market insights
overview = analyzer.create_market_overview()

# Get price recommendations
recommendations = analyzer.generate_price_recommendations(
    category="SUV",
    budget=30000
)

## Data Requirements
Input CSV should contain:

Manufacturer
Model
Production Year
Price
Mileage
Engine Volume
Fuel Type
Category
Leather Interior (Yes/No)

## Dependencies

pandas
numpy
plotly
logging

## License
MIT License

## Author
@nagayahita
gmail: nayahitaaditya@gmail.com
