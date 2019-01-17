from typing import List

def flatten_lists(lst, flattened: List):
    if not isinstance(lst, list):
        flattened.append(lst)
    else:
        for _lst in lst:
            flatten_lists(_lst, flattened)
    return flattened


def print_folder_content(directory, tab_str):
    print(tab_str + str(directory))
    tab_str += '    '
    for dirs in directory.content:
        print_folder_content(dirs, tab_str)


def david_staircase(steps):
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    if steps == 3:
        return 4
    else:
        ways = david_staircase(steps - 1) + david_staircase(steps - 2) + david_staircase(steps - 3)
        return ways


def find_magic_index(lst, start, end):
    if end < start:
        return None
    else:
        mid = (start + end) // 2
        n = lst[mid]
        if mid == n:
            return mid
        elif n < mid:
            return find_magic_index(lst, mid + 1, end)
        elif n > mid:
            return find_magic_index(lst, start, mid - 1)





