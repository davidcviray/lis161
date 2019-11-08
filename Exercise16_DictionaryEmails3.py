filename = input("Enter the file name: ")
fhand = open(filename + ".txt")
count = 0
counts = dict()
words=list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        splitline = line.split()
        strings = splitline[1]
        atpos = strings.find('@')
        endpos = len(strings)
        counts[strings[atpos+1 : endpos]] = counts.get(strings[atpos+1:endpos],0) + 1
print('Counts', counts)
