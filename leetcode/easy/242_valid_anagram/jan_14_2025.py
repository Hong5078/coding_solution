"""
https://leetcode.com/problems/valid-anagram/description/
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    # Initialize hash table with 26 slot, each represent specific letter a-z
    letter_count = [0] * 26
    # index position = ord(character)−ord(’a’)
    # ex. ord('z') - ord('a') == 25, which is 26th letter z
    for i in range(len(s)):
        letter_count[ord(s[i]) - ord('a')] += 1
        letter_count[ord(t[i]) - ord('a')] -= 1

    for i in letter_count:
        if i != 0:
            return False

    return True


if __name__ == "__main__":
    print(is_anagram('eel', 'lee'))
    # Output: True