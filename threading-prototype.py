#!/usr/bin/env python

import threading

class MyT(threading.Thread):
	def __init__(self,args)
		super(MyT,self).__init__()

	def run(self):
		x=worker(args)


if __name__ == "__main__":
	threads = []
	for i in range(num_threads):
		t = MyT(args)
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	