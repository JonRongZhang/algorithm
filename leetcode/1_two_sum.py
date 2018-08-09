# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 2:
            return "At least three numbers."

        l = len(nums)
        for i in range(l):
            if (target - nums[i]) <= 0:
                continue
            for j in range(l):
                if j >= i:
                    break
                elif nums[i] < (target - nums[j]):
                    continue
                elif nums[i] == (target - nums[j]):
                    return [j, i]

    def two_sum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        d = dict()
        l = len(nums)
        for i in range(l):
            d[nums[i]] = i
        for i in range(l):
            complement = target - nums[i]
            if complement in d and complement != i:
                return [i, d[complement]]

    def twosum(self, nums, target):
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        d = dict()
        l = len(nums)
        for i in range(l):
            complement = target - nums[i]
            if complement in d:
                return [d[complement], i]
            d[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    s = Solution()
    # print s.twoSum(nums, 9)
    # print s.two_sum(nums, 9)
    print s.twosum(nums, 9)
