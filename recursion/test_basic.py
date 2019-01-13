import unittest
from recursion.basic import flatten_lists, print_folder_content, david_staircase, find_magic_index
from assertpy import assert_that

class TestBasicRecursion(unittest.TestCase):
    def setUp(self):
        pass

    def test_flatten_list(self):
        lst = [[1, 2], [3, [4, 5, [6]], 7], 8]
        flattened = flatten_lists(lst, [])
        expected = [1,2,3,4,5,6,7,8]
        assert_that(expected).is_equal_to(flattened)

    def test_print_folder_content(self):
        root_dir = _get_test_directories()
        print_folder_content(root_dir,'')

    def test_david_staircase(self):
        assert_that(david_staircase(5)).is_equal_to(13)

    def test_find_magic_index(self):
        lst = [-1, 0, 1, 3, 5, 6, 10, 11, 12, 13]
        assert_that(find_magic_index(lst, 0, len(lst) - 1)).is_equal_to(3)

# helper classes
class Directory:
    def __init__(self, name, content):
        self._name = name
        self._content = content

    @property
    def name(self):
        return self._name

    @property
    def content(self):
        return self._content

    def __repr__(self):
        return self._name

def _get_test_directories():
    file_1 = Directory('file_1', [])
    file_2 = Directory('file_2', [])
    file_3 = Directory('file_3', [])
    file_4 = Directory('file_4', [])
    file_5 = Directory('screenshot_1', [])
    file_6 = Directory('screenshot_2', [])
    dir_1 = Directory('empty', [])
    dir_2 = Directory('dektop', [file_5, file_6])
    dir_3 = Directory('general', [file_3, file_4])
    dir_4 = Directory('recent', [file_1, file_2])
    dir_5 = Directory('files', [dir_4, dir_3])
    root_dir = Directory('root', [dir_1, dir_2, dir_5])
    return root_dir