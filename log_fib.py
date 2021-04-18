# log_fib by Morgan Elder

class LogFib:
    def __init__(self, n=0, f=0):
        self.setLogFib(f)
        self.calcLogFib(n)

    def setLogFib(self, value):
        self._logFig = int(value)

    def getLogFib(self):
        return self._logFig

    def calcLogFib(self,n):
         
        fib = [[0, 1],[1, 1]]
        if n == 0:
            return 0

        self.exponentiateFib(fib, n - 1)
             
        self.setLogFib(fib[1][1])
         
    def multMatrix(self, matrix1, matrix2):
        res = [[0,0],[0,0]]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    res[i][j] += matrix1[i][k] * matrix2[k][j]
         
        for i in range(len(matrix1)):
            for j in range(len(res[0])):
                matrix1[i][j] = res[i][j]
        return matrix1
             

    def exponentiateFib(self, fib, n):
        fibMatrix = [[0, 1],[1, 1]];
        if n >= 0 and n <= 1:
            return;       
        self.exponentiateFib(fib, n // 2)
        fib = self.multMatrix(fib, fib)
        
        if n % 2 != 0: 
            fib = self.multMatrix(fib, fibMatrix)
     




