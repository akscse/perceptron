import numpy as np
class Perecptron:
    def __init__(self, activation):
        self.activation = activation
        return

    def output(self, input_vec, weight, bias):
        '''
            input_vec is numpy array
            weight is numpy matrix
            bias is numpy array
        '''    
        assert type(input_vec) == np.array
        mul_input_weight = input_vec.dot(weight) + bias
        summation_output = self.activation(mul_input_weight)
        output
        return summation_output


