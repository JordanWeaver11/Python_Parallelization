import random as rnd
import time as time
from concurrent.futures import ProcessPoolExecutor as PoolExecutor
from multiprocessing import Lock

#seeds random with system time by default
rnd.seed()

#Global variables
LIST_SIZE = 10000

mutex = Lock()

def do_work(rand_num):
	return rand_num / 3

def main():
	#range(x,y) creates list from x to y, not including y
	#.sample(x,y) chooses y number of unique items from list x
	shared_list = rnd.sample(range(0, LIST_SIZE*10), LIST_SIZE)
	#print(shared_list)

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
	print("\t total time " + str(end_time))

	#Version 2 - Double Thread
	total = 0
	with PoolExecutor(max_workers = 2) as executor:
		start_time = time.process_time()
		for result in executor.map(do_work, shared_list):
			with mutex:
				total += result
		end_time = time.process_time() - start_time
	print("Multithread total: " + str(total))
	print("\t total time " + str(end_time))

main()
