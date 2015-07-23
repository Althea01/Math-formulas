__author__ = 'lily'

#This is a tutorial for adding up numbers in the form of (a,b,c)
import math

def measure(number):
    a = number.split(",")
    return int(a[0])+int(a[1])+int(a[2])


print measure(raw_input("Enter three numbers:\n"))

