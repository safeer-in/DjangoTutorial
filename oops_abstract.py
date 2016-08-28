#!/usr/bin/env python

import abc
class Shape(object):
	__metaclass__ = abc.ABCMeta
	def __init__(self):
		pass

	@abc.abstractmethod
	def get_value(self):
		pass

	@abc.abstractmethod
	def set_value(self,x):
		pass

	@abc.abstractproperty
	def parameter(self):
		pass

	@parameter.setter
	def parameter(self,x):
		pass

	@abc.abstractproperty
	def get_area(self):
		pass


class Square(Shape):
	def __init__(self,x):
		self.x = x

	def set_value(self,x):
		self.x = x

	def get_value(self):
		return self.x

	@property
	def parameter(self):
		return self.x

	@parameter.setter
	def parameter(self,x):
		self.x = x

	def get_area(self):
		return self.x*self.x 


if __name__ == "__main__":
	s= Square(5)
	print s
	print s.set_value(10)
	print s.get_value()

