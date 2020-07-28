#!/usr/bin/env python3
from os import system
from sys import argv
thread = int(argv[1])
mode = str(argv[2])
mode2 = str(argv[3])
for i in range(thread):
    system(
        f"gnome-terminal -e 'bash -c \"python3 TestOnDatasets.py {mode} {mode2}\"'")
