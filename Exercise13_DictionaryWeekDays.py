fhand = open('mbox-short.txt')
count = 0
counts = dict()
words=list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        splitline = line.split()
        counts[splitline[2]] = counts.get(splitline[2],0) + 1
print('Counts', counts)
