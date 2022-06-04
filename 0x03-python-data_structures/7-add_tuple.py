#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    eureka = [tuple_a, tuple_b]
    sum_list = []
    for i in eureka:
        tup_num_count = 0
        if len(i) < 2:
            if len(i) == 0:
                for k in range(2):
                    sum_list.append(0)
            else:
                sum_list.append(i[0])
                sum_list.append(0)
        else:
            for j in i:
                if j:
                    sum_list.append(j)
                    tup_num_count += 1
                elif j == 0:
                    sum_list.append(j)
                    tup_num_count += 1
                else:
                    sum_list.append(0)
                    tup_num_count += 1
                if tup_num_count == 2:
                    break
    stress = (sum_list[0] + sum_list[2], sum_list[1] + sum_list[3])
    return stress
