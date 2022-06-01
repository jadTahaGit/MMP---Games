class Counter:

    def __init__(self):
        self.k = 0
    def count(self):
        self.k += 1
    def reset(self):
        self.k = 0
    def getValue(self):
        return self.k

class LimitCounter(Counter):

    def __init__(self, limit):
        self.k = 0
        self.limit = limit
    def count(self):
        if self.k != self.limit:
            self.k += 1

lc = LimitCounter(4)
print(lc.getValue())
lc.count()
lc.count()
lc.count()
print(lc.getValue())
lc.count()
lc.count()
lc.count()
print(lc.getValue())
