input_fl = 'day2input.txt'
infile = open(input_fl)

def areaPermutations(e):
	a = []
	for i in range(0,len(e)-1):
		for j in range(i+1,len(e)):
			a.append(e[i]*e[j])
	return a

def minimum (a):
	if (len(a) > 0):
		m = a[0]
	else:
	 	m = []
 	for i in (range(1,len(a))):
 		if (a[i] < m):
 			m = a[i]
	return m

total = 0
for line in infile:
	line = line.strip('\n')
	dims = line.split('x')
	dims = map(int, dims)
	faces = areaPermutations(dims)
	for f in faces:
		total = total + 2*f
	total = total + minimum(faces)
#	print(dims, faces, total)

print("Total paper needed = {0}".format(total))

# matt@mattpc:~/aoc2015$ python day1.py
# Floor = 138
