from abc import ABC
import numpy as np

class Constraint(ABC):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def check(self):
        return

class GreaterThan(Constraint):
    def __init__(self, var1, var2):
        super().__init__("%s > %s" % (str(var1), str(var2)))
        self.var1 = var1
        self.var2 = var2

    def check(self):
        if self.var1 == 0 or self.var2 == 0:
            return True
        return self.var1 > self.var2

class LowerThan(Constraint):
    def __init__(self, var1, var2):
        super().__init__("%s < %s" % (str(var1), str(var2)))
        self.var1 = var1
        self.var2 = var2

    def check(self):
        if self.var1 == 0 or self.var2 == 0:
            return True
        return self.var1 < self.var2

class UniqueRow(Constraint):
    def __init__(self, var, row):
        super().__init__("%s unique in %s" % (str(var), str(row)))
        self.var = var
        self.row = row
    
    def check(self):
        return np.count_nonzero(self.row == self.var) == 1