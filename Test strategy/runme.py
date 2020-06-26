from os import system
from sys import argv
thread = int(argv[1])
lenForEach = int(argv[2])
start = int(argv[3])
for i in range(thread):
    system(f"gnome-terminal -e 'bash -c \"python3 TestOnDatasets.py {(i*lenForEach)+start} {((i+1)*lenForEach)+start}\"'")