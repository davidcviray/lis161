def computemin(numbercheck):
    return min(numbercheck)
def computemax(numbercheck):
    return max(numbercheck)

minval = None
maxval = None
values = list()

while True:
    line = input('Enter a number: ')
    if line == 'done' :
            print(computemin(values),computemax(values))
            break
    try:
        input_value = float(line)
        values.append(input_value)
    except ValueError:
        print ("bad data")
