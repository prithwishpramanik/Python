import time
def fib(month,D):
    if month in D:
        return D[month]
    else:
        D[month]=fib(month-1,D)+fib(month-2,D)
        return D[month]
start = time.time()
D={0:1,1:1}
print(fib(500,D))
