class Counter:

    def __init__(self):
        self.k = 0
    def count(self):
        self.k += 1
    def reset(self):
        self.k = 0
    def getValue(self):
        return self.k

c = Counter()
print(c.getValue())
c.count()
c.count()
c.count()
print(c.getValue())
