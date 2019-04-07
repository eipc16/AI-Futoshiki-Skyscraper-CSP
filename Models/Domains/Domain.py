class Domain:
    def __init__(self, domain):
        self.domain = domain

    def in_domain(self, value):
        return domain.contains(value)