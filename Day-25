''' 
    Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum




'''


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        mx=0
        for i in range(n):
            if ( i<= mx < i+1+nums[i] ) :
                if i+nums[i]<n:
                    mx=i+nums[i]
                else:
                    return True
            
        return mx==n-1
