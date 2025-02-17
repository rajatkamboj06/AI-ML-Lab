import numpy as np

file_path = 'test_data.csv'
try:
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)
    
    if data.size == 0:
        raise ValueError("The file is empty or improperly formatted.")
    
    print("Original Data:")
    print(data)
    
    # Handling missing values
    missing_values = np.isnan(data)
    print("Missing Values (True indicates a missing value):")
    print(missing_values)
    
    if np.any(missing_values):
        col_means = np.nanmean(data, axis=0)
        data_cleaned = np.where(np.isnan(data), col_means, data)
    else:
        data_cleaned = data.copy()
    
    print("Data after handling missing values:")
    print(data_cleaned)
    
    # Normalization (Min-Max scaling)
    data_min = np.min(data_cleaned, axis=0)
    data_max = np.max(data_cleaned, axis=0)
    range_values = data_max - data_min
    range_values[range_values == 0] = 1  # Avoid division by zero
    data_normalized = (data_cleaned - data_min) / range_values
    
    print("Data after normalization (Min-Max scaling):")
    print(data_normalized)
    
    # Standardization (Z-score scaling)
    data_mean = np.mean(data_cleaned, axis=0)
    data_std = np.std(data_cleaned, axis=0)
    data_std[data_std == 0] = 1  # Avoid division by zero
    data_standardized = (data_cleaned - data_mean) / data_std
    
    print("Data after standardization (Z-score scaling):")
    print(data_standardized)
    
    # Statistical calculations
    mean = np.mean(data_cleaned, axis=0)
    median = np.median(data_cleaned, axis=0)
    std_dev = np.std(data_cleaned, axis=0)
    variance = np.var(data_cleaned, axis=0)
    
    print("Mean:", mean)
    print("Median:", median)
    print("Standard Deviation:", std_dev)
    print("Variance:", variance)
    
except Exception as e:
    print("Error:", e)
    