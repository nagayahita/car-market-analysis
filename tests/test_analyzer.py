import unittest
import pandas as pd
from src.analyzer import CarMarketAnalyzer

class TestCarMarketAnalyzer(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.DataFrame({
            'Price': [10000, 20000, 30000],
            'Manufacturer_Clean': ['TOYOTA', 'HONDA', 'BMW'],
            'Model': ['Camry', 'Civic', '320i'],
            'Category': ['Sedan', 'Sedan', 'Luxury'],
            'Prod. year': [2018, 2019, 2020]
        })
        self.analyzer = CarMarketAnalyzer(self.test_data)

    def test_market_overview(self):
        overview = self.analyzer.create_market_overview()
        self.assertIsNotNone(overview)
        self.assertIn('Market Size', overview)
        
    def test_recommendations(self):
        recs = self.analyzer.generate_price_recommendations(budget=25000)
        self.assertIsNotNone(recs)
        self.assertTrue(len(recs) > 0)

if __name__ == '__main__':
    unittest.main()
