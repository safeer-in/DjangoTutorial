#!/usr/bin/env python


class Fib(object):

	def __init__(self, m):
		self.n = m
		self.a, self.b = 1, 1

	def __iter__(self):
		if self.n is 0 or self.n is 1:
			yield 1
		else:
			for i in range(2, self.n):
				self.a, self.b = self.b, self.a + self.b
				yield self.b
			raise StopIteration


if __name__ == "__main__":
	f = Fib(10)
	for i in f:
		print i,
	print
	for i in f:
		print i,
	print