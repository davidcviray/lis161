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

lst = []
for key,val in counts.items():
    newtup = (val,key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val,key in lst[:1]:
    print(key, val)
