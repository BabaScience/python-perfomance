import time
from resource import getrusage, RUSAGE_SELF


def long_function():
    for i in range(10 ** 8):
        _ = 2 + 2
        
        
long_function()
print(getrusage(RUSAGE_SELF))