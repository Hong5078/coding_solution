"""
https://leetcode.com/problems/top-k-frequent-elements/
"""


def top_k_frequent(nums, k):
    # Dictionary to count each numbers
    counts = {}

    for n in nums:
        if n not in counts:
            counts[n] = 1
        else:
            counts[n] += 1

    # Method return value in dictionary
    def return_value(key):
        return counts[key]

    # Return the list of key from -k to the end, sort based on value
    return sorted(list(counts.keys()), key = return_value)[-k::]


if __name__ == "__main__":
    print(top_k_frequent([1,2,2,3,3,3], 2))
    # Output: [2, 3]