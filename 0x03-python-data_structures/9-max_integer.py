#!/usr/python3
def max_integer(my_list=[]):
    iter_num = len(my_list)
    if iter_num == 0:
        return None
    break_string = ""
    current_element = my_list[0]
    while break_string != "break":
        step_count = 0
        for i in range(iter_num):
            if my_list[i] < 0:
                my_list[i] *= -1
            sub = current_element - my_list[i]
            step_count += 1
            if sub < 0:
                current_element = my_list[i]
                break
        if step_count == iter_num:
            break_string = "break"
    return current_element
