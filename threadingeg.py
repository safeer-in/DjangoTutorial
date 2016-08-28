#!/usr/bin/env python

import threading
import time
import random

def worker(idnt):
	global lock
	p = random.randint(1,5)
	print "Thread %d started and sleeping for %d"%(idnt,p)
	lock.acquire()
	time.sleep(p)
	lock.release()
	print "Exiting thread %d"%idnt
	return

class MyT(threading.Thread):
	def __init__(self,idnt):
		super(MyT,self).__init__()
		self.idnt = idnt

	def run(self):
		x=worker(self.idnt)


if __name__ == "__main__":
	lock = threading.Lock()
	num_threads = 10
	threads = []
	for i in range(num_threads):
		t = MyT(i)
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	