import matplotlib.pyplot as plt
plt.plot([100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300], [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300])
plt.plot([100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2200, 2300], [10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 220, 230])
plt.xlabel('Number of files')
plt.ylabel('Time in seconds')
plt.show()

from PIL import Image
Image.open('xkcd/all_in_one.png').show()

#Measuring time:
#You can measure time as follows, 
#but the repeat method provided by timeit is recommended because it repeats the measurements several times, then you calculate the minimum as described here: https://realpython.com/sorting-algorithms-python/#the-importance-of-sorting-algorithms-in-python
 
import timeit
start = timeit.timeit()
print("Hello")
end = timeit.timeit()
print(end - start)

import time 
start = time.process_time()
print("Hello")
end = time.process_time()
print(end - start)


