'''
  Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

  Example:

  Input: [0,1,0,3,12]
  Output: [1,3,12,0,0]
  Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
'''

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
      num_zeros = nums.count(0)
      for n in range(num_zeros):  # repeat until all zeros are shifted to the end
          for i in range(len(nums)-1): 
              if nums[i]==0:
                  nums[i],nums[i+1]=nums[i+1],nums[i]	
