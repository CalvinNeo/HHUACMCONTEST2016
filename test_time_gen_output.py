import os, sys
import subprocess
import time

problem = "C"

inp = open(problem + ".in", "rb")
oup = open(problem + ".out", "wb")
start_time = time.time()
stdoutput = subprocess.check_output([problem + ".exe"], stdin=inp)  
end_time = time.time()
oup.write(stdoutput)
print "time cost: {}".format(end_time - start_time)
oup.close()