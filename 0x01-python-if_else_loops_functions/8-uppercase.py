#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            upper_code = ord(char) - ord('a') + ord('A')
            print(chr(upper_code), end="")
        else:
            print(char, end="")
