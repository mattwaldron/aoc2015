input_fl = 'day1input.txt'
infile = open(input_fl)

ups = 0
downs = 0

while (1):
    c = infile.read(1)
    if not c:
        break
    elif c == "(":
        ups = ups + 1
    elif c == ")":
        downs = downs + 1

floor = ups - downs

print("Floor = {0}".format(floor))

# matt@mattpc:~/aoc2015$ python day1.py
# Floor = 138
