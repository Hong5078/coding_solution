"""
https://leetcode.com/problems/group-anagrams/description/
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_groups = {}

    for s in strs:
        # Sort the word to create a key representing its anagram group
        sorted_word = "".join(sorted(s))

        # If the sorted word is not already a key, create a new list
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []

        # Append the original word to the corresponding anagram group
        anagram_groups[sorted_word].append(s)

    # Return the grouped anagrams as a list of lists
    return list(anagram_groups.values())


if __name__ == "__main__":
    list_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(group_anagrams(list_1))
    # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]