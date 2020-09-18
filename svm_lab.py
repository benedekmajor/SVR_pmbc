import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt
import io
import os
import numpy

from multiprocess import Pool


threading_level = 4


class ModelContainer(object):
    def __init__(self, model_description, model_object, result=""):
        self.model_description = model_type
        self.model_object = model_object
        self.result = result


    def save_model(save_path):
        #TODO: save model
        return


def train(data):
    #data contains: [ModelContainer, X, y, predX, predY]
    print("training model: " + data[0].model_description)
    data[0].model_object.fit([data[1], data[2]])
    pred = data[0].model_object.predict(predX)
    miss = predY - pred
    print("training model: " + data[0].model_description + " missed: " + miss)
    return miss



if __name__ == "__main__":
    #for faster results, run test cases parallel
    p = Pool(threading_level)

    #TODO: load data X, y
    X = []
    y = []

    test_model_list = []
    #try the rbf kernel
    test_model_list.append(ModelContainer(model_description="rbf", model_object=SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)))
    #for testing purposes, let's check out different degrees for poly reg
    for i in range(1, 6):
        test_model_list.append(ModelContainer(model_description=str(i) + "_degree_poly", model_object=SVR(kernel='poly', C=100, gamma='auto', degree=3, epsilon=.1, coef0=1)))

    #TODO: make job like: [ModelContainer, X, y, predX, predY]
    job = []

    #pool will not execute jobs in order, but final result will be ordered
    results = p.map(train, job)
