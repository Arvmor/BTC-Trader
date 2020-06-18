import os
thread = int(input("Number of Threads : "))
for i in range(thread):
    os.system("gnome-terminal -e 'bash -c \"python3 TestOnDatasets.py\"'")