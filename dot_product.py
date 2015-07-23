__author__ = 'lily'


#This is a tutorial for dot product of two vectors
import math
def dot_product(vector_a,vector_b):
    a = vector_a.split(",")
    b = vector_b.split(",")
    x1 = int(a[0])
    x2 = int(a[1])
    x3 = int(a[2])
    y1 = int(b[0])
    y2 = int(b[1])
    y3 = int(b[2])
    return x1*y1+x2*y2+x3*y3

print dot_product(raw_input("Enter vector a:\n"),raw_input("Enter vector b:\n"))