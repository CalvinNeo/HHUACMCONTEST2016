
problem = "C"

inp = open(problem + ".dat")
oup = open(problem + ".in", "w+")
times = 2
s = ""
for line in inp:
    line = line.strip("\n")
    if(line == "---"):
        pass
    else:
        s += line
        s += "\n"
for iter in xrange(times):
    oup.write(s)
oup.close()
