import sys 
from rich.console import Console


def JMP(line, dataset):
    return int(line[1])

def TST(line, dataset):
    if 0 >= dataset[line[1]]:
        return 2
    else:
        return 1

def HLT(line, dataset):
    return None

def CRT(line, dataset):
    dataset[line[1]] = 0
    return 1

def DEC(line, dataset):
    tmp = dataset.get(line[1])
    dataset[line[1]] = tmp -1 
    return 1


def INC(line, dataset):
    tmp = dataset.get(line[1])
    dataset[line[1]] = tmp +1 
    return 1

def PRT(line, dataset):
    Console().print(f"[bold cyan]{line[1]}[/bold cyan]: [green]{dataset.get(line[1])}[/green]")
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

def loadFile(filepath):
    with open(filepath, "r") as file:
        return [line.replace("\n", "").split(" ") for line in file.readlines()]


def main():  
    ARGS = sys.argv[1:]

    dataset = {}
    lines = loadFile(ARGS[0])
    
    i = 0
    while i < len(lines):
        line = lines[i]

        if commands.__contains__(line[0]):
            cmd = commands.get(line[0])
            next_line = cmd(line, dataset)
            
            if next_line == None:
                break
            if line[0] == "JMP":
                i = next_line
            else:
                i = i+next_line

if __name__ == "__main__":
    main()