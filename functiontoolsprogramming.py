#!/usr/bin/env python

import functools as fun
import itertools as it

def add(a,b,c):
	return a+b+c 

print add(10,20,30)

print add(c=30,b=20,a=10)

"""
currying
"""
p = fun.partial(add,c=30)
print p(10,20)

q = fun.partial(add,b=20,c=30)
print q(10)


l = range(5)
c = list('abcde')
s='abcde'
p=it.chain(l,c,s)

for i in p:
	print i,

q = it.izip(l,c,s)

for i in q:
	print i,


p = it.imap(lambda x:x*x,l)

for i in p:
	print i,

q = it.ifilter(lambda x:x%2,l)

for i in q:
	print i,

