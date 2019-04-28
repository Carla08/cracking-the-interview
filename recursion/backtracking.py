# and so on, life goes on,
# i dont get recursion,
# but I keep on tryin yooo

def get_all_binary(num_digits: int, output: str):
    """
    num_digits = 3
    000
    001
    010
    011
    100
    101
    """
    if num_digits == 0:
        yield output
    else:
        yield from get_all_binary(num_digits - 1, output + '0')
        yield from get_all_binary(num_digits - 1, output + '1')


def dice_sum(num_dices, _sum, combination):
    """
    num_dices = 2
    sum = 6
    output: {1,5}, {2,4}, {3,3}, {4,2}, {5,1}

    num_dices = 3
    sum = 7
    output: {1,1,5}, {1,2,4}, {1,3,3}, {1,4,2}, {1,5,1}, {2,1,4}, {2,2,3}, {2,3,2}, {2,4,1},
            {3,1,3}, {3,2,2}, {3,3,1}, {4,1,2}, {4,2,1}, {5,1,1}
    """
    if not num_dices:
        return combination
    else:
        for i in range(1, 7):  # 1,2,3,4,5,6
            # choose
            combination.append(i)

            # explore
            _combination = dice_sum(num_dices - 1, _sum, combination)
            if sum(_combination) == _sum and num_dices == 1:
                print(_combination)

            # un-choose
            combination.remove(i)
        return combination


def get_power_set(_set, subset):
    # for each element in the set, create a subset where it is missing.
    # from that other subset create another subset where another is missing.
    if not _set:
        yield subset
    else:
        # choose
        current = _set.pop()
        # choose/explore without current
        yield from get_power_set(_set, subset)
        # choose/explore with current
        subset.add(current)
        yield from get_power_set(_set, subset)
        # unchoose
        _set.add(current)
        subset.remove(current)


num_char_map = {1: ['1'],
                2: ['a', 'b', 'c'],
                3: ['d', 'e', 'f'],
                4: ['g', 'h', 'i'],
                5: ['j', 'k', 'l'],
                6: ['m', 'n', 'o'],
                7: ['p', 'r', 's'],
                8: ['t', 'u', 'v'],
                9: ['w', 'x', 'y'],
                0: ['0']}


def telephone_to_word(nums, word):
    if not nums:
        print(word)
    else:
        num = nums[0]
        del nums[0]
        chars = num_char_map[num]
        for char in chars:
            # choose
            word += char
            # explore
            telephone_to_word(nums, word)
            # unchoose
            word = word[:-1]
        nums.insert(0, num)

telephone_to_word([8,1,2,7,1,7,4,1,7,1], '')
