class BIT:
    """树状数组"""
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

    
class UnionFinder:
    """并查集""""
    def __init__(self, n):
        self.data = [-1] * n
        self.n = n

    def union(self, x, y):
        r1 = self.find(x)
        r2 = self.find(y)

        if r1 == r2:
            return
        if self.data[r1] <= self.data[r2]:
            self.data[r1] += self.data[r2] 
            self.data[r2] = r1
        else:
            self.data[r2] += self.data[r1]
            self.data[r1] = r2
        
    def find(self, x):
        if self.data[x] < 0:
            return x
        p = self.find(self.data[x])
        self.data[x] = p
        return p

    def get_sets(self):
        d = defaultdict(list)
        for i in range(self.n):
            d[self.find(i)].append(i)
        return list(d.values())
