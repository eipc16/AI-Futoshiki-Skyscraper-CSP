class Domain:
    def __init__(self, domain):
        self.domain = domain

    def __str__(self):
        return str(self.domain)

    def in_domain(self, value):
        return domain.contains(value)