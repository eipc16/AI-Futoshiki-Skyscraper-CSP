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

    def __repr__(self):
        return str(self.value)

    def __eq__(self, x):
        return self.value == x.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < x.value

    def __le__(self, other):
        return self.value <= x.value

    def __gt__(self, other):
        return self.value > x.value

    def __ge__(self, other):
        return self.value >= x.value