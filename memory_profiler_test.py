
# run the following commands in the terminal:
# kernprof -l memory_profiler_test.py
# python3 -m memory_profiler memory_profiler_test.py


@profile
def long_function():
    data = []
    for i in range(100000):
        data.append(i)
    return data
    
long_function()