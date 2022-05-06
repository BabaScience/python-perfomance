
# run the following commands in the terminal:
# kernprof -l line_profiler_test.py
# python3 -m line_profiler line_profiler_test.py.lprof


import time



@profile
def long_function():
    print('function start')
    time.sleep(5)
    print('function end')

long_function()