# -*- coding: utf-8 -*-
"""ALATORRE_SOBREVILLA_JULIO_CESAR_Classifying_Iris_Species_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ucY8HWURPYbywG3Skat-yJmmnvRWk8TG

# Introduction to Keras

We are presented with a case of a botanist who wants to classify the iris plant and its derivatives, the objective is to create a model that can learn about them and we can predict the species for a new iris.

#Multi_Layer Perceptron

<center>

![MLP](data:image/jpeg;base64,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)

</center>

Knowing the data of the iris plant will be used to predict the classification options.
The data we will use for this example is the Iris dataset, a classic dataset in machine learning and statistics. It is included in scikit-learn in the data sets module. We can load it by calling the load_iris function:
"""

# Import the Iris dataset
from sklearn.datasets import load_iris
iris_dataset = load_iris()

"""In this section we find the data and commands that are used for this code"""

print("Keys of iris_dataset: \n{}".format(iris_dataset.keys()))

"""After importing the data below the descriptions are used"""

print(iris_dataset['DESCR'][:193] + "\n...")

"""The value of the key target_names is an array of strings, containing the species of
flower that we want to predict:
"""

print("Target names: {}".format(iris_dataset['target_names']))

print("Feature names: \n{}".format(iris_dataset['feature_names']))

print("Type of data: {}".format(type(iris_dataset['data'])))

"""Previously and from here the matrix is thrown"""

print("Shape of data: {}".format(iris_dataset['data'].shape))

print("Shape of data: {}".format(iris_dataset['data'].shape))

print("First five columns of data:\n{}".format(iris_dataset['data'][:5]))

"""From this data, we can see that all of the first five flowers have a petal width of 0.2 cm
and that the first flower has the longest sepal, at 5.1 cm.
The target array contains the species of each of the flowers that were measured, also
as a NumPy array:
"""

print("Type of target: {}".format(type(iris_dataset['target'])))

print("Shape of target: {}".format(iris_dataset['target'].shape))

"""The species are encoded as integers from 0 to 2:"""

print("Target:\n{}".format(iris_dataset['target']))

"""Measuring Success: Training and Testing Data"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
iris_dataset['data'], iris_dataset['target'], random_state=0)

print("X_train shape: {}".format(X_train.shape))
print("y_train shape: {}".format(y_train.shape))

print("X_test shape: {}".format(X_test.shape))
print("y_test shape: {}".format(y_test.shape))

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn import datasets

iris_dataset = datasets.load_iris()
X = iris_dataset.data
Y = iris_dataset.target

iris_dataframe = pd.DataFrame(X, columns=iris_dataset.feature_names)

# Create a scatter matrix from the dataframe, color by y_train
grr = pd.plotting.scatter_matrix(iris_dataframe, c=Y, figsize=(15, 15), marker='o',
                                 hist_kwds={'bins': 20}, s=60, alpha=.8)