#!/usr/bin/env python


class Person(object):
	
	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name
	
	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age):
		self.__age = age

	# def get_name(self):
	# 	return self.__name

	# def get_age(self):
	# 	return self.__age

	# def set_name(self, name):
	# 	self.__name = name

	# def set_age(self, age):
	# 	self.__age = age

	# name = property(get_name, set_name) # property(__gettr__, __settr__)
	# age = property(get_age, set_age)

if __name__ == "__main__":
	p = Person("ABC", 69)
	print p.name, p.age
	p.name = "XYZ"
	p.age = 99
	print p.name, p.age
