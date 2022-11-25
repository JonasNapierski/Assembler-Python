import sys 
from rich.console import Console


def JMP(line: list, dataset: dict) -> int:
    """ JMP jumps to the given line in the assembler code (Note that the document does not start at line 1, but at line 0 as usual).

    :param list line: [name, line-number]
    :param dict dataset: simulated memory for the 'assembler'
    :rtype: int
    :return: line[1] -> line-number 
    """
    return int(line[1])

def TST(line: list, dataset: dict) -> int:
    """f there is a 0 in the memory cell, the program jumps to the 2nd line after the TST & if there is a 1, the program continues in the usual form in the next line.
    
    :param list line: [name, cell]
    :param dict dataset: simulated memory for the 'assembler'
    :rtype: int
    :return: if cell == 0 return 2 else return 1
    """
    if 0 >= dataset[line[1]]:
        return 2
    else:
        return 1

def HLT(line: list, dataset: dict) -> None:
    """HLT aborts the program.

    :param list line: [name, .] **not used**
    :param dict dataset: simulated memory for the 'assembler' **not used**
    :rtype: None
    :return: None 
    """
    return None

def CRT(line: list, dataset: dict) -> int:
    """CRT creates a memory cell with the specified "address".
    
    :param list line: [name, cell] 
    :param dict dataset: simulated memory for the 'assembler'
    :rtype: int
    :return: 1 
    """
    dataset[line[1]] = 0
    return 1

def DEC(line, dataset):
    """DEC decreases the value in a memory cell by 1.
    
    :param list line: [name, cell] 
    :param dict dataset: simulated memory for the 'assembler'
    :rtype: int
    :return: 1 
    
    """
    tmp = dataset.get(line[1])
    dataset[line[1]] = tmp -1 
    return 1


def INC(line: list, dataset: dict) -> int:
    """INC increases the value in a memory cell by 1.

    :param list line: [name, cell] 
    :param dict dataset: simulated memory for the 'assembler'
    :rtype: int
    :return: 1
    """
    tmp = dataset.get(line[1])
    dataset[line[1]] = tmp +1 
    return 1

def PRT(line: list, dataset: dict) -> int:
    """PRT outputs the value in a memory cell.
    
    :param list line: [name, cell] 
    :param dict dataset: simulated memory for the 'assembler'
    :rtype: int
    :return: 1
    """
    Console().print(f"[bright_black]PRINT:[/bright_black] [bold blue_violet]{line[1]}[/bold blue_violet]: [bright_yellow]{dataset.get(line[1])}[/bright_yellow]")
    return 1

def loadFile(filepath: str) -> list:
    """loadFile is used to load a file and parse it into the correct format by adding each argument in a line to a list and which will be added to an output list
    
    :param str filepath: path to the 'assembler' file
    :return: [[line_0[0],line_0[1]],...]
    :rtype: list
    """
    with open(filepath, "r") as file:
        return [line.replace("\n", "").split(" ") for line in file.readlines()]


def main():  
    """ Main function called by using 'python Assembler-Python [file]'
    """
    ARGS = sys.argv[1:]
    loglevel = 0
    if ARGS.__contains__("--loglevel"):
        for i in range(len(ARGS)):
            if ARGS[i] == "--loglevel" and (i+1) <len(ARGS):
                loglevel = int(ARGS[i+1])
    
    commands = {
        "INC": INC,
        "PRT": PRT,
        "CRT": CRT,
        "DEC": DEC,
        "HLT": HLT,
        "JMP": JMP,
        "TST": TST
    }
    dataset = {}
    lines = loadFile(ARGS[0])
    
    i = 0
    while i < len(lines):
        line = lines[i]

        if commands.__contains__(line[0]):
            cmd = commands.get(line[0])
            next_line = cmd(line, dataset)
            
            if loglevel > 0:
                Console().print(f"[bright_black]{'%03d' % i}| {line[1]}[/bright_black]: [bright_yellow]{dataset.get(line[1])}[/bright_yellow]")
            if next_line == None:
                break
            if line[0] == "JMP":
                i = next_line
            else:
                i = i+next_line

if __name__ == "__main__":
    main()