import os
cmd = "cp input.txt output.txt"
iteration = 1
os.system(cmd)
rerun = True
while rerun == True:
    print(iteration)
    cmd = "cp output.txt input1.txt"
    os.system(cmd)
    rerun =  False
    with open("input1.txt") as f1:
        for line in f1:
            if line.split(" ")[1] == '125':
                cmd1 = "cat input1.txt | python mapper.py | sort | python reducer.py | sort > output.txt"
                os.system(cmd1)
                rerun = True
                iteration+=1
                break
    f1.close()
print("Completed the BFS please open the output file")
