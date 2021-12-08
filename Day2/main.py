import re

forward = 0
up = 0
down = 0

with open("data.txt", "r") as file:
    fileData = file.readlines(0)

count = 0
# Strips the newline character
for line in fileData:
    count += 1
    line.strip()
    res = re.split('(\d+)', line)
    direction = res[0]
    mov = int(res[1])
    if direction == 'forward ':
        forward += mov
    elif direction == 'up ':
        up += mov
    elif direction == 'down ':
        down += mov
    else:
        print('Error')

print(forward)
print(up)
print(down)

print((down - up) * forward)

