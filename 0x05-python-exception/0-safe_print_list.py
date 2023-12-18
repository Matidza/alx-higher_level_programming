#!/usr/bin/python3
def safe_print_list(my_list = [], x =0):
    No = 0
    for lst in range(x):
        try:
            print(my_list[lst],)
            No += 1
        except IndexError:
            break
        print('')
        return No
    
safe_print_list()