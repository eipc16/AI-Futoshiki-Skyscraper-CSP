from collections import Iterator

class Domain(Iterator):
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

    def next(self):
        if not self.data:
            raise StopIteration
        return self.data.pop()