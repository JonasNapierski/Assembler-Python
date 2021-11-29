# Willkommen zum Assembler-Python
Dieses Repo beschäftigt sich mit einer ausgedachten / vereinfachten Assmblersprache. Um eine einfacheren Bezug zu der Sprache zuentwickeln, habe ich mich (Jonas Napierski) hingesetzte und schnell in Python einen kleinen Interpreten zu schreiben.

# Befehle

``CRT [cell]``	CRT erstellt eine Speicherzelle  mit der Angegebene "Adresse"
``HLT`` HLT bricht das Programm ab.
``INC [cell]`` INC erhöht den Wert in einer Speicherzelle um 1.
``DEC [cell]`` DEC verringert den Wert in einer Speicherzelle um 1.
``PRT [cell]`` PRT gibt den Wert aus der sich in einer Speicherzelle befindet.
``TST [cell]`` bei einer 0 in der Speicherzelle springt das Prgamm in die 2 Zeile nach dem TST & bei einer  1 geht das Programm in der gewohnten Form in der nächsten Zeile weiter.
``JMP [line]`` JMP Spring zu der angegebene Zeile im Assembler Code (Beachtet das das Dokument nicht bei Zeile 1, sondern Programmier üblich bei Zeile 0 startet!)

# Installation 
Das Script ist getestet in **Python3.8.10**

1. ``$ git clone https://github.com/zirkumflexlab/assembler-python``
2. ``$ cd Assembler-Python``
3. ``$ python -m pip install -r ./requirements.txt`` 


# How to?
Wie benutzt ich das Script, um meine Assembler-Code zu testen?

Einfach geben diesen Befehl ein:
``$ python Assembler-Python.py [path to file]``


# Bugs
Wenn sich das Programm in einer Endlosschleife befindet. versuch das Script abzubrechen unter Windows / Linux  mit [STRG] + c 
