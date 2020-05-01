'''
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1


'''


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return -1
        
        head = 0
        tail =len(nums)-1
        indices = [i for i in range(len(nums))]
        offset=0
        if nums[head]>nums[tail]:   
            while tail>head+1:
                middle=int((head+tail)/2)
                
                if nums[middle]>=nums[head]:
                    head=middle
                else:
                    tail = middle
            #nums = nums[tail:len(nums)]+nums[0:tail]
            #indices = indices[tail:len(nums)]+indices[0:tail]

        
            offset = tail    
        
        
        head = 0
        tail = len(nums)-1
        while tail>head+1:
            middle = int((head+tail)/2)
            if nums[(offset+middle)%len(nums)]>=target:
                tail=middle
            else:
                head = middle

        if nums[(offset+tail)%len(nums)]==target:
            return indices[(offset+tail)%len(nums)]
        elif nums[(offset+head)%len(nums)]==target:
            return indices[(offset+head)%len(nums)]            
        else:
            return -1
        
