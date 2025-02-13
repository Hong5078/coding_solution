"""
https://leetcode.com/problems/contains-duplicate/
"""


def contains_duplicate(nums):
    dup = {}

    for n in nums:
        if n not in dup:
            dup[n] = 1

        else:
            dup[n] += 1

    for n in dup:
        if dup[n] > 1:
            return True

    return False


if __name__ == '__main__':
    list_1 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

    print(contains_duplicate(list_1))