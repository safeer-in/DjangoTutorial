#!/usr/bin/env python

import multiprocessing
import time
import random

def worker(idnt):
	global lock
	p=random.randint(1,5)
	print "Process %d started and sleeping for %d seconds"%(idnt,p)
	lock.acquire()
	time.sleep(p)
	lock.release()
	print "existing process %d"%idnt
	return


class MyP(multiprocessing.Process):
	"""Multiprocessing example"""
	def __init__(self, idnt):
		super(MyP, self).__init__()
		self.idnt = idnt

	def run(self):
		x=worker(self.idnt)

if __name__ == "__main__":
	lock = multiprocessing.Lock()
	num_tasks = 10
	jobs = []
	for i in range(num_tasks):
		p= MyP(i)
		jobs.append(p)
		p.start()

	for p in jobs:
		p.join()

print "Finished"
		