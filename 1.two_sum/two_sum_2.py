nums = [2,7,11,15]
target = 9


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicc = {}
        for i, n in enumerate(nums):
            diff = target -n
            if diff in dicc:
                return [dicc[diff], i]
            dicc[n] = i

solution = Solution()
print(solution.twoSum(nums,target))