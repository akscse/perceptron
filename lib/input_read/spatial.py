import numpy as np

class Spatial:
    def __init__(self, space_coord):
        self.space = np.array(space_coord)
        return

    def get_space(self):
        return self.space
