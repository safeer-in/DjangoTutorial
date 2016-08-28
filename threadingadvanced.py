#!/usr/bin/env python

import threading
import time
import random
import Queue

def worker(idnt,q):
	while True:
		t=q.get()
		if t==None:
			break
		else:
			p = random.randint(1,5)
			print "Thread %d started and sleeping for %d"%(idnt,p)
			time.sleep(p)
			print "Finished task %d"%idnt
	return

class MyT(threading.Thread):
	def __init__(self,idnt,q):
		super(MyT,self).__init__()
		self.idnt = idnt
		self.q =q

	def run(self):
		x=worker(self.idnt,self.q)


if __name__ == "__main__":
	lock = threading.Lock()
	num_tasks = 10
	num_workers = 3
	q = Queue.Queue()

	for i in range(num_tasks):
		q.put(i)

	#poison pill technique
	for i in range(num_workers):
		q.put(None)

	threads = []
	for i in range(num_workers):
		t = MyT(i,q)
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	