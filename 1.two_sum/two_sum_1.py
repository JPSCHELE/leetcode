nums = [2,7,11,15]
target = 9


class Solution(object):
    def give_index(self,array, target):
        for i in range(len(array)-1):
            for j in range(i+1, len(array)):
                if array[i] + array[j] == target:
                    return [i,j]


solution= Solution()
print(solution.give_index(nums,target))