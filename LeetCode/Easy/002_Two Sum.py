class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic ={}
        for i, j in enumerate(nums):
            num = target-j
            if num in dic:
                return [dic[num], i]
            dic[j]=i

print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))