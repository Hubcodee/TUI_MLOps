import numpy as np      
import pandas as pd 
from sklearn.linear_model import LogisticRegression   
from sklearn.model_selection import train_test_split
import sys

def read_csv_dataset(file_path):        
    # Read the .csv file and return a pandas DataFrame
    return pd.read_csv(file_path)

def LogR(data):
    data.drop(['PassengerId', 'Name', 'Cabin', 'Ticket'], axis=1, inplace=True)
    data['Age'].fillna(data['Age'].mean(), inplace=True)
    sex = pd.get_dummies(data["Sex"], drop_first=True)
    embark = pd.get_dummies(data["Embarked"], drop_first=True)
    pclass = pd.get_dummies(data["Pclass"], drop_first=True)
    data.drop(["Sex", "Embarked", "Pclass"], axis=1, inplace=True)
    data = pd.concat([data, sex, embark, pclass], axis=1)
    data.columns = data.columns.astype(str)
    X = data.drop("Survived", axis=1)
    Y = data["Survived"]
    np.unique(Y)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    log_reg = LogisticRegression(max_iter=1000, C=0.1)
    log_reg.fit(X_train, y_train)
    log_reg.score(X_test, y_test)
    log_reg.score(X_train, y_train)
    return log_reg.coef_,log_reg.intercept_

if __name__=="__main__":
    filename = sys.argv[1]
    df = read_csv_dataset(filename)
    slope,intercept = LogR(df)
    dataw = f"""
        Slope (m): {slope}
        Intercept (b): {intercept}
    """
    filepath = "result.txt"
    with open(filepath,'w') as f:
        f.write(dataw)





