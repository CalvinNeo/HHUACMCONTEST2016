#coding:utf8
import random
from math import pi, sin, cos, asin, acos
import math

xy_lim = 100

def gen_p(n):
    pts = []
    for i in xrange(n):        
        x = random.randint(0, xy_lim)
        y = random.randint(0, xy_lim)
        if not (x, y) in pts:
            pts.append((x, y))
    return (len(pts), sorted(pts, cmp = lambda p1, p2: cmp(p1[1] , p2[1]) if p1[0] == p2[0] else cmp(p1[0] , p2[0])))

#def add_polygon(point_count, n):
#    br = []
#    for i in xrange(point_count):  
#        b = None
#        while(b == None or b in br):
#            b = random.randint(1, n)
#        br.append(b)
#    br.sort()
#    poly = []
#    for i in xrange(len(br) - 1):
#        poly.append((br[i], br[i + 1]))
#    poly.append((br[i + 1], br[0]))
#    return poly

#def add_onecase(poly_counts, n_count):
#    points = []
#    edges = []
#    n, points = gen_p(n_count)
#    m = 0
#    for point_count in poly_counts:
#        new_edges = add_polygon(point_count, n)
#        for e in new_edges:
#            if not e in edges:
#                edges.append(e)
#    return points, edges

def get_rad(p, o):
    dx = p[0] - o[0]
    dy = p[1] - o[1]
    dr = (dx ** 2 + dy ** 2) ** 0.5
    sinx = dy / dr
    cosx = dx / dr
    if dx > 0 and dy > 0:
        # 1
        return asin(sinx)
    elif dx < 0 and dy > 0:
        # 2
        # sin(x - pi / 2) = - cos x
        return asin(-cosx) + pi / 2
    elif dx < 0 and dy < 0:
        # 3
        # cos(x - pi) = - cos x
        return acos(-cosx) + pi
    elif dx > 0 and dy < 0:
        # 4
        # cos(x - 3 pi / 2) = cos(pi - (x - pi / 2)) = - cos(x - pi / 2) = - sinx
        return acos(-sinx) + 3 * pi / 2
    elif dx == 0 and dy > 0:
        # axis y +
        return pi / 2
    elif dx == 0 and dy < 0:
        # axis y -
        return 3 * pi / 2
    elif dy == 0 and dx > 0:
        # axis x +
        return 0
    elif dy == 0 and dx < 0:
        # axis x - 
        return pi
    else:
        # zero point
        return None

def sort_by_radius(psi):
    avrx = sum([p[0][0] for p in psi]) / len(psi)
    avry = sum([p[0][1] for p in psi]) / len(psi)
    #print [p[0][0] for p in psi]
    #print [p[0][1] for p in psi]
    print avrx, avry
    prads = [(p[0][0], p[0][1], get_rad((p[0][0], p[0][1]), (avrx, avry)), p[1]) for p in psi]
    sorted_pr = sorted(prads, cmp = lambda x, y: cmp(x[2], y[2]))
    return sorted_pr


def add_polygon2(point_count, n, points):
    poly = []
    # 在points中随机抽取point_count个点
    pindexs = random.sample(range(n), point_count)
    psi = [(points[i], i) for i in pindexs]
    # 根据对中心的弧度逆时针排序
    sortedps = sort_by_radius(psi)
    print [(p[0], p[1], p[2] / pi * 180, p[3]) for p in sortedps]
    print points
    for i in xrange(len(sortedps) - 1):
        poly.append((sortedps[i][3], sortedps[i + 1][3]))
    poly.append((sortedps[0][3], sortedps[len(sortedps) - 1][3]))
    return poly


def add_onecase2(poly_counts, n_count):
    points = []
    edges = []
    n, points = gen_p(n_count)
    m = 0
    for point_count in poly_counts: 
        # 在points中选取point_count个点添加一个多边形
        new_edges = add_polygon2(point_count, n, points) 
        for e in new_edges:
            if not e in edges:
                edges.append(e)
    return points, edges

def print_case(ps, es, fo):
    fo.write("{} {}\n".format(len(ps), len(es)))
    for p in ps:            
        fo.write("{} {}\n".format(p[0], p[1]))
    for p in es:            
        fo.write("{} {}\n".format(p[0] + 1, p[1] + 1))


def datagen():
    max_edges = 0
    fo = open("C.big.dat", "w+")
    point_count = [3, 4, 5, 6, 7, 8, 15, 17] # 每个多边形具有的点数
    for n in [30, 40, 50]: # 总点数
        ps, es = add_onecase2(point_count, n)
        max_edges = max(len(es), max_edges) # 最多的边数，用来开数组
        print_case(ps, es, fo)

    point_count = [30, 40, 50, 60] # 每个多边形具有的点数
    for n in [100, 130, 150, 200]: # 总点数
        ps, es = add_onecase2(point_count, n)
        max_edges = max(len(es), max_edges) # 最多的边数，用来开数组
        print_case(ps, es, fo)

    fo.close()
    print max_edges


#print get_rad((0, -1), (0, 0)) / pi * 180

datagen()
exit()

#n, points = gen_p(10)
#print n
#for p in points:
#    print p
#print add_polygon(4)