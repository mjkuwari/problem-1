# Reverse String
class Solution(object):
    def reverseString(self, s):
        return s.reverse()
    
# Two Sum
class Solution(object):
  def twoSum(self, nums, target):
    output = []
    for i in range(len(nums)):
      for j in range(len(nums)):
        if nums[i] + nums[j] == target and i != j:
          output.append(i) 
          output.append(j)         
          return output
        
# Search Insert Position: Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
class Solution(object):
    def searchInsert(self, nums, target):
        output = 0
        for i in range(len(nums)):
            if nums[i] == target:
                output = i
        if output == 0:
            for i in range(len(nums)):
                if target < nums[i]:
                    output = i
                    break
            if output == 0:
                output = len(nums)
        return output
