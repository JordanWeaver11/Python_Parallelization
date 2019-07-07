import random as rnd
import time as time
from concurrent.futures import ProcessPoolExecutor as PoolExecutor

#seeds random with system time by default
rnd.seed()

#Global variables
LIST_SIZE = 10



def do_work(lower_bound, upper_bound, shared_list):
	total = 0
	#add total for each element in bounded list
	for x in shared_list[lower_bound:upper_bound]:
		total += x / 3
	return total

def main():
	#range(x,y) creates list from x to y, not including y
	#.sample(x,y) chooses y number of unique items from list x
	shared_list = rnd.sample(range(0, LIST_SIZE*10), LIST_SIZE)
	print(shared_list)

	#Version 1 - Single Thread
	#start timer
	start_time = time.process_time()
	total = 0
	#do work
	for x in shared_list:
		total += x / 3
	#end timer
	end_time = time.process_time() - start_time
	print("Single thread total: " + str(total))
	#print(end_time)

	#Version 2 - Double Thread
	#thread1. Does work on lower half of list
	lower_bound = 0
	upper_bound = int(LIST_SIZE/2)
	thread1_total = do_work(lower_bound, upper_bound, shared_list)
	print("Thread 1 total: " + str(thread1_total))
	
	#thread2. Does work on upper half of list
	lower_bound = int(LIST_SIZE/2)
	upper_bound = int(LIST_SIZE)
	thread2_total = do_work(lower_bound, upper_bound, shared_list)
	print("Thread 2 total: " + str(thread2_total))
	
	

main()
