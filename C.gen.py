#coding:utf8
import random

xy_lim = 100

def gen_p(n):
    pts = []
    nn = 0
    for i in xrange(n):        
        x = random.randint(0, xy_lim)
        y = random.randint(0, xy_lim)
        if not (x, y) in pts:
            pts.append((x, y))
            nn += 1
    return (nn, sorted(pts, cmp = lambda p1, p2: cmp(p1[1] , p2[1]) if p1[0] == p2[0] else cmp(p1[0] , p2[0])))

def add_polygon(point_count, n):
    br = []
    for i in xrange(point_count):  
        b = None
        while(b == None or b in br):
            b = random.randint(1, n)
        br.append(b)
    br.sort()
    poly = []
    for i in xrange(len(br) - 1):
        poly.append((br[i], br[i + 1]))
    poly.append((br[i + 1], br[0]))
    return poly

def add_onecase(poly_counts, n_count):
    points = []
    edges = []
    n, points = gen_p(n_count)
    m = 0
    for point_count in poly_counts:
        new_edges = add_polygon(point_count, n)
        for e in new_edges:
            if not e in edges:
                edges.append(e)
    return points, edges

def print_case(ps, es, fo):
    fo.write("{} {}\n".format(len(ps), len(es)))
    for p in ps:            
        fo.write("{} {}\n".format(p[0], p[1]))
    for p in es:            
        fo.write("{} {}\n".format(p[0], p[1]))


def datagen():
    max_edges = 0
    fo = open("C.bit.dat", "w+")
    point_count = range(5, 16) * 2
    for n in [30, 40, 50, 70, 90, 110, 130, 150, 200]:
        ps, es = add_onecase(point_count, n)
        max_edges = max(len(es), max_edges)
        print_case(ps, es, fo)
    fo.close()
    print max_edges
datagen()

#n, points = gen_p(10)
#print n
#for p in points:
#    print p
#print add_polygon(4)