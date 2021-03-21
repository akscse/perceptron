import numpy as np

class Sigmoid:
    def __init__(self):
        return
    def execute(self, input):
        output = 1/(1+np.exp(-input))
        return output