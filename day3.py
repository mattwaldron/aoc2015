input_fl = 'day3input.txt'
infile = open(input_fl)

class col():
    def __init__(self, i, v):
        self.idx = i
        self.cnt = 1
        self.vals = []
        self.vals.append(v)
    def appendunique(self, v):
        for x in self.vals:
            if (x == v):
                return
        self.vals.append(v)
        self.cnt = self.cnt + 1
    def getcnt(self):
        return self.cnt
    def getidx(self):
        return self.idx

def visit(c, r):
#   print("visiting house {0}, {1}".format(c,r))
    global hgrid
    for h in hgrid:
        if (c == h.getidx()):
            h.appendunique(r)
            return
    hgrid.append(col(c,r))
    return

x = 0
y = 0

hgrid = []
visit(x, y)

while (1):
    ch = infile.read(1)
    if not ch:
        break
    if (ch == '>'):
        x = x + 1
    elif (ch == '<'):
        x = x - 1
    elif (ch == 'v'):
        y = y - 1
    elif (ch == '^'):
        y = y + 1
    else:
        print ("Bad character in directions")
#   print(ch)
    visit(x,y)

total = 0
for h in hgrid:
#   print(h.idx, h.vals)
    total = total + h.getcnt()

print("Unique houses visited = {0}".format(total))

# matt@mattpc:~/aoc2015$ python day3.py
# Unique houses visited = 2565
