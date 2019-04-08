
import numpy as np

class Constraint():
    def __init__(self):
        pass
        
    def check(self):
        return

class GreaterThan(Constraint):
    def __init__(self, var1, var2):
        super().__init__()
        self.var1 = var1
        self.var2 = var2

    def check(self):
        if self.var1.value == 0 or self.var2.value == 0:
            return True
        return self.var1.value > self.var2.value

    def get_constrained(self):
        return self.var2

    def __str__(self):
        return "%s > %s" % (str(self.var1), str(self.var2))

class LowerThan(Constraint):
    def __init__(self, var1, var2):
        super().__init__()
        self.var1 = var1
        self.var2 = var2

    def check(self):
        if self.var1.value == 0 or self.var2.value == 0:
            return True
        return self.var1.value < self.var2.value

    def get_constrained(self):
        return self.var2

    def __str__(self):
        return "%s < %s" % (str(self.var1), str(self.var2))

class Unique(Constraint):
    def __init__(self, var, row):
        super().__init__()
        self.var = var
        self.row = row
    
    def check(self):
        return self.var.value == 0 or np.count_nonzero(self.row == self.var.value) < 2

    def get_constrained(self):
        return self.row

    def __str__(self):
        return "%s unique in %s" % (str(self.var), str(self.row))
