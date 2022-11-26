import numpy as np

class Perceptron:

    def __init__(self, alpha=0.01, n_iters = 1000):
        self.alpha = alpha
        self.n_iters = n_iters
        self.activation_func = self.unit_step_func
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.n_iters):
            for index, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights)+self.bias 
                y_predicted = self.activation_func(linear_output)

                update = self.alpha * (y_[index]-y_predicted)
                self.weights = self.weights + update * x_i
                self.bias = self.bias + update


    def predict(self, X):
        linear_output = np.dot(X, self.weights) +self.bias
        y_predicted = self.activation_func(linear_output)
        return  y_predicted


    def unit_step_func(self, x):
        return np.where(x>=0, 1,0)