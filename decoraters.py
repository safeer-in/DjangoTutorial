#!/usr/bin/env python


def mk_inc(m):
	def inc(n):
		return m+n
	return inc


if __name__ == "__main__":
	p = mk_inc(10)
	q = mk_inc(100)
	print p(10), q(10)
	print p.__closure__[0].cell_contents
	print q.__closure__[0].cell_contents