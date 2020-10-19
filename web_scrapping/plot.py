import matplotlib.pyplot as plt
plt.autoscale(True)
plt.plot([100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300], [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300])
plt.plot([100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300], [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 220, 230])
plt.xlabel('Number of files')
plt.ylabel('Time in seconds')
plt.show()

# from PIL import Image
# Image.open('xkcd/all_in_one.png').show()

#Measuring time:
#You can measure time as follows, 
#but the repeat method provided by timeit is recommended because it repeats the measurements several times, then you calculate the minimum as described here: https://realpython.com/sorting-algorithms-python/#the-importance-of-sorting-algorithms-in-python
 
import time 
start = time.process_time()
print("Hello")
end = time.process_time()
print(end - start)

# import matplotlib.pyplot as plt
# plt.plot([100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300], [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300])
# plt.plot([100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300], [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 220, 230])
# plt.xlabel('Number of files')
# plt.ylabel('Time in seconds')
# plt.show()

# from PIL import Image
# Image.open('xkcd/all_in_one.png').show()

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

#option: function as text
# setup_code = '''
# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n-1)
# '''

from timeit import repeat
def run_algorithm(algorithm, n):
    #To give the timeit module access to functions you define, you can pass a setup parameter which contains an import statement:    
    setup_code = f"from __main__ import {algorithm}" 
    
    #call to the function factorial as text
    times = repeat(f"{algorithm}({n})", setup = setup_code, repeat=3, number=1000) #repeats the execution 
    #Pay attention to the fact that the output is the execution time of number times iteration of the code snippet, not the single iteration. 
    # For a single iteration exec. time, divide the output time by number.

    return times

for n in range(10, 1000, 100):
    times = min(run_algorithm("factorial", n))
    print (times) #seconds



