#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("item lis {:x}".format(my_list[i], end=" "))
            count += 1
    except:
        break
        
print()
return count