#!/usr/bin/python3
for i in range(0, 10):
    for d in range(i, 10):
        if (i == d):
            continue
        elif (i == 8 and d == 9):
            print(f"{i}{d}", end='\n')
        elif (i != d):
            print(f"{i}{d}", end=', ')
