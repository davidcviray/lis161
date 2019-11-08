filename = input("Enter the file name: ")
fhand = open(filename + ".txt")
count = 0
counts = dict()
words=list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        splitline = line.split()
        counts[splitline[1]] = counts.get(splitline[1],0) + 1
print('Counts', counts)
