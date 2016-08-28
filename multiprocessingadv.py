#!/usr/bin/env python

import multiprocessing
import time
import random

def worker(idnt,q):
	while True:
		t=q.get()
		if(t==None):
			break
		else:
			p=random.randint(1,5)
			print "Process %d started and sleeping for %d seconds"%(idnt,p)
			time.sleep(p)
			print "existing process %d"%idnt
	return


class MyP(multiprocessing.Process):
	"""Multiprocessing example"""
	def __init__(self, idnt,q):
		super(MyP, self).__init__()
		self.idnt = idnt
		self.q =q 

	def run(self):
		x=worker(self.idnt,self.q)

if __name__ == "__main__":
	lock = multiprocessing.Lock()
	num_tasks = 10
	num_workers = multiprocessing.cpu_count()
	q = multiprocessing.JoinableQueue()
	for i in range(num_tasks):
		q.put(i)

	for i in range(num_workers):
		q.put(None)
	jobs = []
	for i in range(num_workers):
		p= MyP(i,q)
		jobs.append(p)
		p.start()

	for p in jobs:
		p.join()

print "Finished"
		