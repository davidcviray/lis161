import string

filename = input("Enter the file name: ")
fhand = open(filename + ".txt")

counts = 0
dct = dict()
lst = list()

for line in fhand:
    line = line.translate(str.maketrans('','',string.digits))
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()

    words = line.split()
    for word in words:
        for letter in word:
            counts += 1
            if letter not in dct:
                dct[letter] = 1
            else:
                dct[letter] += 1

for key, val in list(dct.items()):
    lst.append((val,key))

lst.sort(reverse=True)

for key,val in lst:
    print(key,val)
