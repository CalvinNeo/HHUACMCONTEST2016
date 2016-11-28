#coding:utf8
import random

def seq(n, s):
    # n numbers sum up to s
    br = []
    for i in xrange(n):
        b = None
        while(b == None or b in br):
            b = random.randint(1, s)
        br.append(b)
    br.sort()
    ans = [br[0]]
    for i in xrange(n - 1):
        ans.append(br[i+1] - br[i])
    return ans

def datagen():
    fo = open("A.big.dat", "w+")
    #for i in xrange(10, 15):
    #    for j in xrange(300, 1000, 100):
    #for i in [100, 200, 300]:
    #    for j in [8000, 9000, 10000]:
    for (i, j) in [(300, 10000), (50, 1000), (100, 2000), (130, 3000), (150, 4000), (200, 5000), (250, 6000)]:
        weights = seq(i, j)
        values = [random.randint(1, 400) for xx in xrange(i)]
        print len(weights), len(values)
        fo.write("{} {}\n".format(i, j))
        for ii in xrange(i):
            fo.write("{} {}\n".format(str(values[ii]), str(weights[ii])))
    fo.close()

datagen()