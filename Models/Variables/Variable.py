class Variable:
    def __init__(self, value, predefined=False):
        self.value = value
        self._prev_value = value
        self.predefined = predefined

    def update(self, value):
        if predefined != True:
            self._prev_value = self.value
            self.value = value
        else:
            print("You can't change this variable (%s)" % str(self))    

    def rollback(self):
        if predefined != True:
            self.value = self._prev_value
        else:
            print("You can't change this variable (%s)" % str(self))  