
class Solution:
    def twoSum1(self, nums, target):
        
        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums):
                if (i + j) == target and index_i != index_j:
                    return [index_i ,index_j]

    def twoSum2(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

obj = Solution()
print(obj.twoSum2([1,3,3], 6))
