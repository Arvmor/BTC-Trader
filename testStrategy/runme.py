#!/usr/bin/env python3
from os import system
from sys import argv
thread = int(argv[1])
for i in range(thread):
    system(f"gnome-terminal -e 'bash -c \"python3 TestOnDatasets.py dataset\"'")
