import sys
for line in sys.stdin:
    line = line[:len(line)-1]
    inputData = line.split(' ')
    distanceToAdd = int(inputData[1]) +1;
    pointsTo = inputData[2][:len(inputData[2])-1].split(':')
    for i in range(0,len(pointsTo)):
        print(str(pointsTo[i])+ " VALUE " +str(distanceToAdd));
    print(str(inputData[0])+ " VALUE " +str(inputData[1]));
    print(str(inputData[0])+ " NODES " +str(inputData[2]));
