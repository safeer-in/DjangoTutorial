#!/usr/bin/env python


class Iter(object):
	def __init__(self, m, n):
		self.c = m - 1
		self.n = n

	def __iter__(self):
		return self

	# def __next__(self):

	def next(self):
		# while self.m < self.n
		# 	yield self.m
		# 	self.m += 1
		# raise StopIteration(" error")
		self.c += 1
		if self.c > self.n:
			raise StopIteration
		else:
			return self.c


if __name__ == "__main__":
	I = Iter(10,20)
	for i in I:
		print I.next()
		