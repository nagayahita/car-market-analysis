class CarMarketAnalyzer:

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.market_insights = {}
        self._calculate_market_metrics()

    def _calculate_market_metrics(self):

        try:

            self.market_insights['price_metrics'] = {
                'avg_price': self.data['Price'].mean(),
                'median_price': self.data['Price'].median(),
                'min_price': self.data['Price'].min(),
                'max_price': self.data['Price'].max(),
                'price_std': self.data['Price'].std()
            }


            manufacturer_stats = self.data.groupby('Manufacturer_Clean').agg({
                'Price': ['mean', 'count', 'std'],
                'Mileage_Clean': 'mean',
                'Vehicle_Age': 'mean'
            }).round(2)

            self.market_insights['manufacturer_stats'] = manufacturer_stats

        except Exception as e:
            logger.error(f"Error calculating market metrics: {str(e)}")
            raise

    def create_market_overview(self) -> Dict:

        try:
            overview = {
                "Market Size": {
                    "Total Vehicles": len(self.data),
                    "Total Manufacturers": self.data['Manufacturer_Clean'].nunique(),
                    "Total Categories": self.data['Category'].nunique()
                },
                "Price Overview": {
                    "Average Price": f"${self.market_insights['price_metrics']['avg_price']:,.2f}",
                    "Median Price": f"${self.market_insights['price_metrics']['median_price']:,.2f}",
                    "Price Range": f"${self.market_insights['price_metrics']['min_price']:,.2f} - "
                                 f"${self.market_insights['price_metrics']['max_price']:,.2f}"
                },
                "Top Manufacturers": self._get_top_manufacturers(),
                "Popular Categories": self._get_category_insights()
            }
            return overview

        except Exception as e:
            logger.error(f"Error creating market overview: {str(e)}")
            raise

    def _get_top_manufacturers(self, top_n: int = 5) -> Dict:

        try:
            top_by_price = self.data.groupby('Manufacturer_Clean')['Price'].mean().nlargest(top_n)
            top_by_volume = self.data.groupby('Manufacturer_Clean').size().nlargest(top_n)

            return {
                "Most Expensive": {name: f"${price:,.2f}" for name, price in top_by_price.items()},
                "Most Popular": {name: count for name, count in top_by_volume.items()}
            }

        except Exception as e:
            logger.error(f"Error getting top manufacturers: {str(e)}")
            raise

    def _get_category_insights(self) -> Dict:

        try:
            category_stats = self.data.groupby('Category').agg({
                'Price': ['mean', 'count']
            })

            return {
                "By Average Price": {
                    cat: price for cat, price in
                    category_stats['Price']['mean'].nlargest(5).round(2).items()
                },
                "By Popularity": {
                    cat: int(count) for cat, count in
                    category_stats['Price']['count'].nlargest(5).items()
                }
            }

        except Exception as e:
            logger.error(f"Error getting category insights: {str(e)}")
            raise

    def create_interactive_visualizations(self):

        try:

            fig1 = px.histogram(self.data, x='Price',
                              title='Price Distribution',
                              template='plotly_white')
            fig1.show()


            fig2 = px.scatter(self.data, x='Prod. year', y='Price',
                             color='Manufacturer_Clean',
                             title='Price vs Production Year',
                             template='plotly_white')
            fig2.show()


            fig3 = px.box(self.data, x='Category', y='Price',
                          title='Price Distribution by Category',
                          template='plotly_white')
            fig3.show()

        except Exception as e:
            logger.error(f"Error creating visualizations: {str(e)}")
            raise

    def generate_price_recommendations(self, category: str = None, budget: float = None) -> pd.DataFrame: # Corrected indentation

        try:
            recommendations = self.data.copy()

            if category:
                recommendations = recommendations[recommendations['Category'] == category]
            if budget:
                recommendations = recommendations[recommendations['Price'] <= budget]

            if len(recommendations) == 0:
                logger.warning(f"No vehicles found matching criteria: category={category}, budget=${budget:,}")
                return pd.DataFrame()

            recommendations['Value_Score'] = (
                (1 - recommendations['Price'] / recommendations['Price'].max()) * 0.3 +  # Lower price is better
                (1 - recommendations['Mileage_Clean'] / recommendations['Mileage_Clean'].max()) * 0.3 +  # Lower mileage is better
                (1 - recommendations['Vehicle_Age'] / recommendations['Vehicle_Age'].max()) * 0.2 +  # Newer is better
                (recommendations['Is_Luxury'].fillna(0) * 0.2)

            )

            top_picks = recommendations.nlargest(5, 'Value_Score')[[
                'Manufacturer_Clean', 'Model', 'Price', 'Prod. year',
                'Mileage_Clean', 'Category', 'Fuel_Type_Clean', 'Value_Score'
            ]]

            return top_picks

        except Exception as e:
            logger.error(f"Error generating recommendations: {str(e)}")
            raise
print("\n🚙 TOP CATEGORIES BY PRICE:")
for category, price in overview["Popular Categories"]["By Average Price"].items():
    print(f"• {category}: ${price:,.2f}")
