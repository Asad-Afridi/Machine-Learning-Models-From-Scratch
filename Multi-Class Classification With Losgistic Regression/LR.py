import numpy as np
import matplotlib.pyplot as plt
class LogisticRegression():
    
    def __init__(self,lr = 0.001,epochs = 1000):
        self.lr = lr
        self.epochs = epochs
        self.weight = None
        self.bias = None
        cost = []
        it = []
    def fit(self, X, y):
        no_of_samples,no_of_features = X.shape
        self.weight = np.zeros(no_of_features)
        self.bias = 0
        cost = []
        it = []
        for i in range(self.epochs):
            z = np.dot(X,self.weight) + self.bias
            z = np.clip(z, -500, 500)
            y_pred = 1 / (1 + np.exp(-z))
            y_pred = np.clip(y_pred, 1e-10, 1 -1e-10)
            dw = np.dot(X.T,y_pred - y)
            db = np.sum(y_pred - y)

            self.weight = self.weight - self.lr * (dw)
            self.bias = self.bias - self.lr * (db)
            
                        
            # for y = 1
            y1 =  y*np.log(y_pred)
            #for y = 0
            y0 = (1-y) * np.log(1-y_pred)
            
            los = (-1/no_of_samples) * (np.sum(y1 + y0))
            cost.append(los)
        return cost
    def predict(self,X):
        z = np.dot(X,self.weight) + self.bias
        z = np.clip(z, -500, 500)
        y_pred = 1 / (1 + np.exp(-z))
        return y_pred