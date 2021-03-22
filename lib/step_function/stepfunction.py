class StepFunction:
    def __init__(self):
        return

    def output(self, y):
        try: 
            float(y)
        except: 
            return "Invalid Input. Must be int or float"
        return 1 if y > 0 else 0