preprocessor = DataPreprocessor()


processed_train = preprocessor.process_dataset(train_data, is_training=True)
processed_test = preprocessor.process_dataset(test_data, is_training=False)


print("Sample of processed training data:")
display(processed_train.head())
