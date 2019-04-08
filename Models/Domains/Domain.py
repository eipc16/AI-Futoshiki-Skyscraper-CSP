from collections import Sequence
import random as r

class Domain(Sequence):
    def __init__(self, domain):
        self.domain = domain

    def __str__(self):
        return str(self.domain)

    def in_domain(self, value):
        return domain.contains(value)

    def remove(self, value):
        self.domain.remove(value)

    def append(self, value):
        self.domain.append(value)

    def copy(self):
        return Domain([i for i in self.domain])

    def __getitem__(self, index):
        return self.domain[index]

    def __len__(self):
        return len(self.domain)

    def shuffled(self):
        r.shuffle(self.domain)
        return self.domain