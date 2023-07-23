import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import sys

def read_csv_dataset(file_path):        
    # Read the .csv file and return a pandas DataFrame
    return pd.read_csv(file_path)

def simple_linear_regression(X, y):
    # Create a Linear Regression model and fit it to the data
    print("Creating model Linear Regression model....")
    model = LinearRegression()
    model.fit(X, y)

    # Get the slope and intercept of the regression line
    slope = model.coef_[0]
    intercept = model.intercept_

    return slope, intercept

def predict(X, slope, intercept):
    return slope * X + intercept

if __name__ == "__main__":
    # Replace 'your_dataset.csv' with the path to your .csv file
    filename = sys.argv[1]

    # Read the dataset from the .csv file
    df = read_csv_dataset(filename)

    # Extract the independent variable (X) and dependent variable (y)
    X = df['YearsExperience'].values.reshape(-1, 1)
    y = df['Salary'].values

    # Perform simple linear regression
    slope, intercept = simple_linear_regression(X, y)
    dataw = f"""
        Slope (m): {slope}
        Intercept (b): {intercept}
    """
    filepath = "result.txt"
    with open(filepath,'w') as f:
        f.write(dataw)
    






