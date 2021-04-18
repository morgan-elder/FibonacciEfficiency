#lin_fib

class LinFib:
    def __init__(self, n=0, f=0):
        self.setLinFib(f)
        self.calcLinFib(n)

    def setLinFib(self, value):
        self._linFib = int(value)

    def getLinFib(self):
        return self._linFib
    
    def calcLinFib(self, n):
    
        knownF1 = 0
        knownF2 = 1
        
        if n == 0:
            fib = 0
        elif n == 1:
            fib = 1
        elif n > 1:
            for i in range(n):        
                fib = knownF1 + knownF2
                knownF2 = knownF1
                knownF1 = fib
        self.setLinFib(fib)


