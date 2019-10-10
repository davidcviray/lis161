filename = input("Enter the file name: ")
if filename=="na na boo boo":
    print('Here is a funny message')
else:
    fhand = open(filename + ".txt")
    count = 0
    average = 0
    for line in fhand:
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence:') :
            count = count +1
            data = float(line[20:])
            average = average + data
    print('Average spam confidence: ', average/count)
        
