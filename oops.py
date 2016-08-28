#!/usr/bin/env python

import re

class Date(object):

	def __init__(self,year,month,day):
		self.year = year
		self.month = month
		self.day = day

	@classmethod
	def fromString(cls,st):
		rx = re.compile('[-/]')
		day,month,year = rx.split(st)
		d = Date(int(year),int(month),int(day))
		return d

	@staticmethod
	def is_valid(year,month,day):
		if year < 1970 or year > 2050:
			return False
		if month < 1 or month > 12: return False
		if day < 1 or day > 31: return False
		return True

	def get_date(self):
		return(self.year,self.month,self.day)

if __name__=="__main__":
	d=Date(2016,8,18)
	print d.get_date()

	d1 = Date.fromString("18/08/2016")
	print d1.get_date()
	print Date.is_valid(d1.year,d1.month,d1.day)