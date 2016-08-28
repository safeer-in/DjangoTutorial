#!/usr/bin/env python

import re

num = ['2342',hex(2342),oct(2342),'56432',hex(56432)]
#numpattern = '^[-+]?[0-9]+' 
#numpattern = '\d'
numpattern = '^0[xX][0-9a-fA-F]+' #hex numbers
rx = re.compile(numpattern)
txt = "the quick brown fox jumped over a lazy dog"
#pattern = 'fox'
pattern = '[aeiou]'
# match = re.search(pattern,txt)
# if match:
# 	print txt,"-->",match.start(),match.end()
# else:
# 	print "Not matched"


# for match in re.finditer(pattern,txt):
	# print txt,"-->",match.start(),match.end()," char is",txt[match.start():match.end()]

for x in num:
	# if re.search(numpattern,x):
	if re.search(rx,x):
		print x
	else:
		pass


