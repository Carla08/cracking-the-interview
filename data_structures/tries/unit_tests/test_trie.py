import unittest
from assertpy import assert_that

from data_structures.tries.trie import Trie

class TestTrie(unittest.TestCase):

    def test_insert_word_in_empty_trie(self):
        trie = Trie()
        trie.add_word("carla")

    def test_insert_word_in_existing_trie(self):
        trie = Trie()
        trie.add_word("carla")
        trie.add_word("carlos")

    def test_is_in_trie(self):
        trie = Trie()
        trie.add_word("carla")
        assert_that(trie.is_in_trie("carla")).is_true()

    def test_is_not_in_trie(self):
        trie = Trie()
        trie.add_word("carlos")
        assert_that(trie.is_in_trie("carla")).is_false()
