from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from keras.layers import Dense
from keras.models import Sequential
import sys 

def read_csv_dataset(file_path):        
    # Read the .csv file and return a pandas DataFrame
    return pd.read_csv(file_path)

def ANN_mod(data):
    data = data.drop(['CustomerId', 'Surname', 'RowNumber'], axis = 1)
    x = data.iloc[:,0:10]
    y = data.iloc[:,10]
    x = pd.get_dummies(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.fit_transform(x_test)
    x_train = pd.DataFrame(x_train)
    
    model = Sequential()
    model.add(Dense(units = 8,activation = 'relu',bias_initializer="zeros",
                    kernel_initializer="zeros", input_dim = 13))
    model.add(Dense(units = 8,bias_initializer="zeros",
                    kernel_initializer="zeros", activation = 'relu'))
    model.add(Dense(units = 8, bias_initializer="zeros",
                    kernel_initializer="zeros", activation = 'relu'))
    model.add(Dense(units = 8, bias_initializer="zeros",
                    kernel_initializer="zeros", activation = 'relu'))
    model.add(Dense(units = 8, bias_initializer="zeros",
                    kernel_initializer="zeros", activation = 'relu'))
    model.add(Dense(units = 1, bias_initializer="zeros",
                    kernel_initializer="zeros", activation = 'sigmoid'))
    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']) 
    model.fit(x_train, y_train, epochs = 10)
    def build_classifier():
      # creating the model
      model = Sequential()

      # first hidden layer
      model.add(Dense(units = 8,  activation = 'relu', input_dim = 13))

      # second hidden layer
      model.add(Dense(units = 8, activation = 'relu'))

      # output layer
      model.add(Dense(units = 1,  activation = 'sigmoid'))

      # Compiling the NN
      # binary_crossentropy loss function used when a binary output is expected
      model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

      return model

    model = KerasClassifier(build_fn = build_classifier, batch_size = 10, nb_epoch = 10)
    accuracies = cross_val_score(estimator = model, X = x_train, y = y_train, cv = 10, n_jobs = -1)
    print("Accuracies :", accuracies)

    print("Mean Accuracy :", accuracies.mean())
    print("Variance :", accuracies.std())
    return accuracies, accuracies.mean(), accuracies.std()

if __name__=="__main__":
  filename = sys.argv[1]
  df = read_csv_dataset(filename)
  accuracy_mod,accuracy_mean,accuracy_std = ANN_mod(df)
  dataw = f"""
      accuracy_mod: {accuracy_mod}
      accuracy_mean: {accuracy_mean}
      accuracy_std: {accuracy_std}
  """
  filepath = "result.txt"
  with open(filepath,'w') as f:
    f.write(dataw)





