class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        kv = 0  
        svm = 0 
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l): 
                if nums[i] + nums[j] == target:
                    kv = i
                    svm = j
                    return [kv, svm]
        return [kv, svm] 