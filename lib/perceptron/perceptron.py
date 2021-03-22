import numpy as np
import sys

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
        try:
            assert type(input_vec) == type(np.array([]))
            mul_input_weight = input_vec.dot(weight) + bias
            out = [self.activation(val) for val in mul_input_weight].sum()
            return out
        except AssertionError:
            return "input_vec not a numpy array"
        except:
            err = sys.exc_info()[0]
            return f"Error occured: {err}"