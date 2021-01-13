"""
author: Dominik Stec,
index:  s12623,
email:  s12623@pja.edu.pl
To run module type:
 >> python SVC_Pima_diabetes.py
as Python interpreter command
pandas, numpy and scikit-learn modules installation is need
This module read Pima indians diabetes data, fit SVC algorithm, and test algorithm accurancy.
"""

from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


class SVCPimaDiabetes:
    """
    This class read Pima indians diabetes data from *.csv raw, split data to train and test set,
    fit SVC algorithm to get classification result, test algorithm with test data and return fit accurancy.
    """

    __pima = None
    __X = None
    __y = None
    __svc = None
    __X_test = None
    __y_test = None

    def load_dataset(self):
        """This method read raw data from csv file into pandas dataframe object,
            next map read object to numpy array
        """
        self.__pima = pd.read_csv('pima_indians_diabetes.csv', delimiter=',')
        np_pima = np.array(self.__pima)
        self.__X, self.__y = np_pima[:, :-1], np_pima[:, -1]

    def fit_data(self):
        """This method split data to train and test set, after that fit SVC algorithm by train data
        """
        X_train, self.__X_test, y_train, self.__y_test = train_test_split(self.__X, self.__y, test_size=0.25)
        self.__svc = svm.SVC(kernel='linear', gamma=80).fit(X_train, y_train)

    def test_data(self):
        """This method test algorithm fit accurancy

        Returns:
            float: value of algorithm classification accurancy
        """
        score = self.__svc.score(self.__X_test, self.__y_test)
        return score


diabetes_classification = SVCPimaDiabetes()
diabetes_classification.load_dataset()
diabetes_classification.fit_data()
print('\nclassification accurancy = ', diabetes_classification.test_data())