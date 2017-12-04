#!/usr/bin/env python


def tharb(x, y):
	return x * y


try:

	math = int(raw_input("Write First Number "))

except (ValueError):
	print ("Write Number only")
try:

	math1 = int(raw_input("Write Second Number "))

except (ValueError):
	print ("Write Number only")

else:

	print (math, "*", math1, "=", tharb(math,math1))
