# Day1 of Advent of code. - COMPLETED


count = 0
token = 1

with open("data.txt", "r") as f:
    dataFile = f.read() # Read all file in case values are not on a single line
    data_ints = [ int(x) for x in dataFile.split() ] # Convert strings to ints
    rep = (len(data_ints)) - 1
    for x in range(rep):

        if data_ints[token] > data_ints[token-1]:
            count += 1
            token += 1
        else:
            token += 1

print(count)
