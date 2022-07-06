#!/usr/bin/python3
'''Module that prints out pascal's trinagle'''


def pascal_triangle(n):
    '''Returns a paswcal triangle'''
    if n <= 0:
        return []
    count = 1
    tri_list = []
    ele_list = []
    for i in range(n):
        print("ran")
        if count == 1:
            ele_list.append(1)
            tri_list.append(ele_list)
            ele_list = []
        else:
            ele_list.append(1)
            former = tri_list[count - 2]
            for j in range(len(former)):
                if j + 1 == len(former):
                    break
                else:
                    ele_list.append(former[j] + former[j + 1])
            ele_list.append(1)
            tri_list.append(ele_list)
            ele_list = []
        count += 1
    return tri_list
