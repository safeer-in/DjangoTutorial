#!/usr/bin/env python

# def outer_p(a, b):
# 	def outer(fun):
# 		def inner(x,y):
# 			if x < a: x = a
# 			if x > b: x = b
# 			if y < a: y = a
# 			if y > b: y = b
# 			return fun(x,y)
# 		return inner
# 	return outer

class Outer(object):
	def __init__(self,fun):
		self.fun = fun

	def __call__(self,p,q):
		if p<100 : p =100
		if p>200 : p =200
		if q<100 : q =100
		if q>200 : q =200
		return self.fun(p,q)

@Outer
def add(p,q):
	return p+q

# add = outer(add)


if __name__ == "__main__":
	print add(-1000, 150)
	print add(120, 250)
