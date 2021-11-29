# Welcome to Assembler-Python 
This repo deals with an invented / simplified assmbler language. To develop a simpler reference to the language, I (Jonas Napierski) sat down and quickly wrote a small interpreter in Python.
[German version](https://github.com/zirkumflexlab/Assembler-Python/blob/master/README.md)
# Commands
- ``CRT [cell]`` CRT creates a memory cell with the specified "address".
- ``HLT`` HLT aborts the program.
- ``INC [cell]`` INC increases the value in a memory cell by 1.
- ``DEC [cell]`` DEC decreases the value in a memory cell by 1.
- ``PRT [cell]`` PRT outputs the value in a memory cell.
- ``TST [cell]`` If there is a 0 in the memory cell, the program jumps to the 2nd line after the TST & if there is a 1, the program continues in the usual form in the next line.
- ``JMP [line]`` JMP jumps to the given line in the assembler code (Note that the document does not start at line 1, but at line 0 as usual).

# Install
The script is tested in **Python3.8.10**

1. ``$ git clone https://github.com/zirkumflexlab/assembler-python``
2. ``$ cd Assembler-Python``
3. ``$ python -m pip install -r ./requirements.txt``

# How to use

How do I use the script to test my assembler code? Simply enter this command:
``$ python Assembler-Python.py [path to file]``

# Bugs
If the program is in an endless loop. try to abort the script under Windows / Linux with [CTRL] + c
