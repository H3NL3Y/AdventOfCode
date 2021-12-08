
column1 = ''
gam = ''
#epsilom = ''

with open("data.txt", "r") as file:
    fileData = file.readlines(0)

count = 0
# Strips the newline character

for i in range(5):

    for line in fileData:
        line.strip()
        column1 = column1 + line[i]
        bin1 = column1.count('1')
        bin0 = column1.count('0')
        #count += 1

    if bin1 > bin0:
        gam = gam + '1'
    else:
        gam = gam + '0'

    #count = count + 1


print(gam)










