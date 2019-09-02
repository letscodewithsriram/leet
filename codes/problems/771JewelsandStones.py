"""
771. Jewels and Stones

You're given strings J representing the types of stones

that are jewels, and S representing the stones you have.

Each character in S is a type of stone you have.

You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:-
S and J will consist of letters and have length at most 50.
The characters in J are distinct.

"""

# Using Naive Algorithm
# Runtime: 32 ms, faster than 93.51% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.5 MB, less than 5.39% of Python3 online submissions for Jewels and Stones.


def num_jewels_in_stones(jewel_stones, all_stones) -> int:
    """
    Function identifies the no of valid jewel stones in the club of stones.

    :param jewel_stones: [string] - Stones which can be used as Jewels
    :param all_stones: [string] - All stones includes Jewel Stones & Non-Jewel Stones
    :return: [integer] - Count of Jewel making stones
    """
    # print("Jewel Stones: {}; Stones: {}".format(jewel_stones, all_stones))

    jewel_stones = jewel_stones.rstrip()
    all_stones = all_stones.rstrip()

    total_jewel_count = 0

    for jewel_stone in jewel_stones:
        total_jewel_count = total_jewel_count + all_stones.count(jewel_stone)

    return total_jewel_count


print(num_jewels_in_stones("aA", "aAAbbbb"))


# Using Lambda Functions
# Runtime: 40 ms
# Memory Usage: 13.9 MB

def num_jewels_in_stones_ul(jewel_stones, all_stones) -> int:
    """
    Function identifies the no of valid jewel stones in the club of stones.

    :param jewel_stones: [string] - Stones which can be used as Jewels
    :param all_stones: [string] - All stones includes Jewel Stones & Non-Jewel Stones
    :return: [integer] - Count of Jewel making stones
    """

    return sum(list(map(lambda jewel_stone: all_stones.count(jewel_stone), jewel_stones)))


print(num_jewels_in_stones_ul("aA", "aAAbbbb"))
