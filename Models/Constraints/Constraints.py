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


class SkyscraperRule(Constraint):
    def __init__(self, row, left_constraint, right_constraint, orientation):
        super().__init__()
        self.row = row
        self.left_constraint = left_constraint
        self.right_constraint = right_constraint
        self.orientation = orientation

    def check(self):
        highest_left_, highest_right_ = 0, 0
        count_left_, count_right_ = 0, 0

        size = self.row.shape[0]

        for i in range(size):

            var_value_left_ = self.row[i].value
            var_value_right_ = self.row[size - i - 1].value

            if var_value_left_ == 0 or var_value_right_ == 0:
                return True

            if highest_left_ < var_value_left_:
                #print(' %d | %d' % (highest_left_, var_value_left_))
                highest_left_ = var_value_left_
                count_left_ += 1

            if highest_right_ < var_value_right_:
                highest_right_ = var_value_right_
                count_right_ += 1

        left_check = self.left_constraint == 0 or count_left_ == self.left_constraint
        right_check = self.right_constraint == 0 or count_right_ == self.right_constraint

        #print('L/T: %d, R/B: %d, ROW: %s, LEFT: %s, RIGHT: %s' % (self.left_constraint, self.right_constraint, str(self.row), str(left_check), str(right_check)))

        return left_check and right_check

    def get_constrained(self):
        return self.vars

    def __str__(self):
        (left, right) = ("Left", "Right") if self.orientation == "h" else ("Top", "Bottom")
        return "Row: %s | %s: %s | %s: %s |" % (str(self.row), left, str(self.left_constraint), right, str(self.right_constraint))
