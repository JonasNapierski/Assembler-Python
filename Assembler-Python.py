import sys 
from rich.console import Console

con = Console()

ARGS = sys.argv[1:]

dataset = {}
lines = []

def JMP(line):
    return int(line[1])

def TST(line):
    if 0 >= dataset[line[1]]:
        return 2
    else:
        return 1

def HLT(line):
    return None

def CRT(line):
    dataset[line[1]] = 0
    return 1

def DEC(line):
    tmp = dataset.get(line[1])
    dataset[line[1]] = tmp -1 
    return 1


def INC(line):
    tmp = dataset.get(line[1])
    dataset[line[1]] = tmp +1 
    return 1

def PRT(line):
    con.print(f"[bold cyan]{line[1]}[/bold cyan]: [green]{dataset.get(line[1])}[/green]")
    return 1


commands = {
    "INC": INC,
    "PRT": PRT,
    "CRT": CRT,
    "DEC": DEC,
    "HLT": HLT,
    "JMP": JMP,
    "TST": TST
}

def loadFile():
    file = open(ARGS[0], "r")
    tmpLines = file.readlines()

    for line in tmpLines:
        line = line.replace("\n", "")
        lines.append(line.split(" "))

loadFile()
i = 0
while i < len(lines):
    line = lines[i]

    if commands.__contains__(line[0]):
        cmd = commands.get(line[0])
        next_line = cmd(line)
        
        if next_line == None:
            break
        if line[0] == "JMP":
            i = next_line
        else:
            i = i+next_line
        #con.print("Something went wrong.", style="bold red")
