"""
771. Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.  The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

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

def numJewelsInStones(J, S) -> int:
    """
    Function identifies the no of valid jewel stones in the club of stones.

    :param J: [string] - Stones which can be used as Jewels
    :param S: [string] - All stones includes Jewel Stones & Non-Jewel Stones
    :return: [integer] - Count of Jewel making stones
    """
    # print("Jewel Stones: {}; Stones: {}".format(J, S))

    jewel_stones = J.rstrip()
    stones = S.rstrip()

    total_jewel_count = 0

    for jewel_stone in jewel_stones:
        total_jewel_count = total_jewel_count + stones.count(jewel_stone)

    return total_jewel_count


print(numJewelsInStones("aA", "aAAbbbb"))


# Using Lambda Functions
# Runtime: 40 ms
# Memory Usage: 13.9 MB

def numJewelsInStones(J, S) -> int:
    """
    Function identifies the no of valid jewel stones in the club of stones.

    :param J: [string] - Stones which can be used as Jewels
    :param S: [string] - All stones includes Jewel Stones & Non-Jewel Stones
    :return: [integer] - Count of Jewel making stones
    """

    return sum(list(map(lambda jewel_stones: S.count(jewel_stones), J)))


print(numJewelsInStones("aA", "aAAbbbb"))