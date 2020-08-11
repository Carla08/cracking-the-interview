import unittest
from assertpy import assert_that

from data_structures.tries.trie_problems import BadKeyboard

class TrieProblems(unittest.TestCase):

    def test_bad_keyboard(self):
        """
        The Question:
        There is a broken keyboard in which space gets typed when you type the letter 'e'. Given an input string which
        is the output from the keyboard. A dictionary of possible words is also provided as an input parameter of the
        method. Return a list of possible actual input typed by the user.

        Example Input: String: "can s r n " Dictionary: ["can", "canes", "serene", "rene", "sam"]
        Expected Output: ["can serene", "canes rene"]
        """

        keyboard = "can s r n "
        dictionary = {"can", "canes", "serene", "rene", "sam"}
        expected_output = ["can serene", "canes rene"]

        bad_keyboard = BadKeyboard(dictionary)
        bad_keyboard.solve(keyboard)
        assert_that(expected_output).is_equal_to(bad_keyboard.get_solved())
