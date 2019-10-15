fhand = open('mbox-short.txt')
count = 0
words=list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        splitline = line.split()
        print(splitline[1])
        count = count + 1
print(count, 'lines in the file with From as the first word')
