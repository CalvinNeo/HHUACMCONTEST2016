
problem = "D"

def gen_file(inp):
    s = ""
    for line in inp:
        line = line.strip("\n")
        if(line[0:3] == "---"):
            pass
        elif line[0:2] == "**":
            pass
        elif line == "":
            pass
        else:
            s += line
            s += "\n"
    return s

inps = open(problem + ".small.dat", "r+")
inpb = open(problem + ".big.dat", "r+")
#oupdat = open(problem + ".dat", "w+")
oup = open(problem + ".in", "w+")

s = ""
s += gen_file(inps)
s += gen_file(inpb)

times = 3
for iter in xrange(times):
    oup.write(s)
oup.close()
