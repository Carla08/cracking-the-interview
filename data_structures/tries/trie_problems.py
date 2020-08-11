from data_structures.tries.trie import Trie


class BadKeyboard:
    """
    The Question:
    There is a broken keyboard in which space gets typed when you type the letter 'e'. Given an input string which
    is the output from the keyboard. A dictionary of possible words is also provided as an input parameter of the
    method. Return a list of possible actual input typed by the user.

    Example Input: String: "can s r n " Dictionary: ["can", "canes", "serene", "rene", "sam"]
    Expected Output: ["can serene", "canes rene"]
    """

    def __init__(self, dictionary):
        self.solved = False
        # build a trie from the dictionary
        root_trie = Trie(dictionary)
        self.root = root_trie.root

        # to keep track of the tries that are being processed.
        self.tries = [self.root]

        # save output
        self.output = [""]

    def solve(self, keyboard):
        # for each char in the keyboard check if there's a word
        for char in keyboard:
            if char == " ":  # it might be the end of a word or an e or both
                self.traverse_tries(Trie.EOW)
                self.traverse_tries("e")
            else:
                self.traverse_tries(char)
        self.solved = True

    def traverse_tries(self, c):
        for i, trie in enumerate(self.tries):
            if c in trie.children:
                output_str = self.output[i]
                self.output[i] += c
                if c == Trie.EOW:
                    self.tries[i] = self.root
                    if len(trie.children) > 1:
                        self.output.append(output_str)
                        self.tries.append(trie)
                    break
                self.tries[i] = trie.children[c]

    def get_solved(self):
        if self.solved:
            return [s.replace(Trie.EOW, " ") for s in self.output]
