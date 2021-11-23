import sys 

#args = sys.argv[:1]
lines = [["CRT","100"]]
def CRT(line):
    dataset[line[1]] = 0

def INC(line):
    tmp = dataset.get(line[1])
    dataset[line[1]] = tmp +1 

def PRT(line):
    print(dataset.get(line[1]))

commands = {
    "INC": INC,
    "PRT": PRT,
    "CRT": CRT
}
dataset = {
    
}

for line in lines:
    if commands.__contains__(line[0]):
        commands.get(line[0])