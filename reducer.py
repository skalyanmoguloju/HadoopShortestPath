import sys
prev = -1
lower = 125
nodes = "UNMODED"
for line in sys.stdin:
    inputData = line.split(' ')
    if prev == -1:
        prev = int(inputData[0])
        lower = 125
    if int(inputData[0]) != prev:
        print(str(prev) +" "+str(lower)+" "+str(nodes[:len(nodes)-1]))
        prev = int(inputData[0])
        lower = 125
        nodes = "UNMODED"
    if inputData[1] == "NODES":
        nodes = inputData[2]
    else:
        distance = int(inputData[2])
        lower = min(distance, lower)
