class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        point = 0
        for i in range(len(nums)):
            if nums[i]!=nums[i-1]:
                nums[point]=nums[i]
                point+=1
        return point if point>0 else 1