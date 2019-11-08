filename = input("Enter the file name: ")
fhand = open(filename + ".txt")
count = 0
counts = dict()
words=list()
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        splitline = line.split()
        strings = splitline[5]
        colonpos = strings.find(':')
        counts[strings[:colonpos]] = counts.get(strings[:colonpos],0) + 1

lst = []
for key,val in counts.items():
    newtup = (key,val)
    lst.append(newtup)

lst = sorted(lst)

for val,key in lst:
    print(val,key)
