"""
https://leetcode.com/problems/3sum/description/
"""


def three_sum(nums):
    output = []
    nums.sort()

    for i in range(len(nums)):
        ## (D1) Duplicate case handle 1
        if i > 0 and nums[i] == nums[i - 1]:
            continue ##

        j = i + 1
        k = len(nums) - 1

        while j < k:
            sum_3 = nums[i] + nums[j] + nums[k]
            if sum_3 < 0:
                j += 1
            elif sum_3 > 0:
                k -= 1
            else:
                output.append([nums[i], nums[j], nums[k]])

                j += 1
                k -= 1
                ## (D2) Duplicate case handle 2
                while nums[j] == nums[j - 1] and j < k:
                    j += 1 ##

    return output

if __name__ == "__main__":
    l = [-4, -1, -1, -1, 0, 1, 1, 2, 2]

    print(three_sum(l))