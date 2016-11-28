#coding:utf8
import random
from math import pi, sin, cos, asin, acos
import math


#fo = open("C.big.dat", "r+")
fo = open("temp.txt", "r+")
fw = open("C.cad.dat", "w+")
vn, en = map(int, fo.readline().split())
v = []
for i in xrange(vn):
    x, y = map(int, fo.readline().split())
    v.append((x, y))
fw.write( "erase\nall\n\n" )
for i in xrange(en):
    a, b = map(int, fo.readline().split())
    fw.write( "line\n" )
    fw.write( "{},{}\n".format(v[a - 1][0], v[a - 1][1]) )
    fw.write( "{},{}\n".format(v[b - 1][0], v[b - 1][1]) )
    fw.write( "\n" )
fo.close()
fw.close()
quit()