"""
https://leetcode.com/problems/two-sum/description/
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    # Dictionary to store the numbers we've seen and their corresponding indices
    history = {}

    # Iterate through the list with both the number and its index
    for index, num in enumerate(nums):
        # Calculate the complementary number required to reach the target
        complement = target - num

        # Check if the complement is in the dictionary
        if complement in history:
            # If found, return the indices of the complement and the current number
            return [history[complement], index]

        # If not, store the current number and its index in the dictionary
        history[num] = index

    # Return an empty list if no solution is found
    return []


if __name__ == '__main__':
    nums_list = [2, 7, 11, 15, 19]

    print(two_sum(nums_list, 21))
    # Output: [0, 4]

    nums_list_2 = [3,2,4]

    print(two_sum(nums_list_2, 6))
    # Output: [1, 2]

    nums_list_3 = [3,3]

    print(two_sum(nums_list_3, 6))
    # Output: [0, 1]