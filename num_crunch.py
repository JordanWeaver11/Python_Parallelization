import random as rnd
import time as time
from concurrent.futures import ProcessPoolExecutor as PoolExecutor

LIST_SIZE = 1000000
#seeds random with system time by default
rnd.seed()

#range(x,y) creates list from x to y, not including y
#.sample(x,y) chooses y number of unique items from list x
rand_list = rnd.sample(range(0, LIST_SIZE*10), LIST_SIZE)
#print(rand_list)

start_time = time.process_time()
total = 0
for x in rand_list:
	total += x / 333.1
end_time = time.process_time() - start_time

print(total)
print(end_time)
