class BIT:
    def __init__(self, n):
        self.data = [0] * (n + 1)
        self.n = n
    
    def update(self, i, val):
        while i <= self.n:
            self.data[i] += val
            i += i & -i
    
    def query(self, i):
        res = 0
        i = min(i, self.n)
        while i > 0:
            res += self.data[i]
            i -= i & -i
        return res
