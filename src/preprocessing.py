class DataPreprocessor:

    def __init__(self):
        self.errors = []
        self.warnings = []

    def clean_numeric_field(self, value: str, field_type: str) -> float:

        try:
            if pd.isna(value):
                return 0.0

            if field_type == 'mileage':
                return float(str(value).replace('km', '').strip())

            elif field_type == 'engine':

                numeric_part = ''.join(char for char in str(value) if char.isdigit() or char == '.')
                return float(numeric_part) if numeric_part else 0.0

            elif field_type == 'price':
                return float(value)

        except Exception as e:
            self.errors.append(f"Error cleaning {field_type} value '{value}': {str(e)}")
            return 0.0

    def clean_categorical_field(self, value: str, field_type: str) -> str:

        try:
            if pd.isna(value):
                return 'Unknown'

            value = str(value).strip().upper()

            if field_type == 'manufacturer':

                manufacturer_map = {
                    'VW': 'VOLKSWAGEN',
                    'MERCEDES': 'MERCEDES-BENZ'
                }
                return manufacturer_map.get(value, value)

            elif field_type == 'fuel_type':

                fuel_map = {
                    'PETROL': 'GASOLINE',
                    'DIESEL': 'DIESEL',
                    'HYBRID': 'HYBRID',
                    'ELECTRIC': 'ELECTRIC'
                }
                return fuel_map.get(value, value)

            return value

        except Exception as e:
            self.errors.append(f"Error cleaning {field_type} value '{value}': {str(e)}")
            return 'Unknown'

    def process_dataset(self, df: pd.DataFrame, is_training: bool = True) -> pd.DataFrame:

        try:
            processed_df = df.copy()


            processed_df['Mileage_Clean'] = processed_df['Mileage'].apply(
                lambda x: self.clean_numeric_field(x, 'mileage')
            )
            processed_df['Engine_Volume_Clean'] = processed_df['Engine volume'].apply(
                lambda x: self.clean_numeric_field(x, 'engine')
            )


            processed_df['Manufacturer_Clean'] = processed_df['Manufacturer'].apply(
                lambda x: self.clean_categorical_field(x, 'manufacturer')
            )
            processed_df['Fuel_Type_Clean'] = processed_df['Fuel type'].apply(
                lambda x: self.clean_categorical_field(x, 'fuel_type')
            )


            current_year = datetime.now().year
            processed_df['Vehicle_Age'] = current_year - processed_df['Prod. year']
            processed_df['Is_Luxury'] = processed_df['Leather interior'].map({'Yes': 1, 'No': 0})

            if is_training:

                processed_df['Price_Per_Year'] = processed_df['Price'] / processed_df['Vehicle_Age']
                processed_df['Price_Per_Mile'] = processed_df['Price'] / processed_df['Mileage_Clean']

            return processed_df

        except Exception as e:
            logger.error(f"Error processing dataset: {str(e)}")
            raise
