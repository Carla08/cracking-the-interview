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
