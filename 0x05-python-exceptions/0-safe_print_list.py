#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for idx, element in enumerate(my_list[:x]):
            if idx < x - 1:
                print(element, end="")
            else:
                print(element)
            count += 1
    except IndexError:
        print()
        return count
    return count

