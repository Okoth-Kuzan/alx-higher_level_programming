#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        print("{}{}".format(a, b), end=", " if int(str(a) + str(b)) < 89 else "\n")
