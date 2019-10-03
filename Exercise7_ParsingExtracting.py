string = 'X-DSPAM-Confidence:0.8475'
colonpos = string.find(':')
endpos = len(string)
data = float(string[colonpos+1 : endpos])
print(data)
