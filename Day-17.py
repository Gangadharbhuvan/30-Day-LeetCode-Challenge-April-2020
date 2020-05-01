'''
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution:
    def numIslands(self, nums: List[List[str]]) -> int:
        visited = [[False] * len(x) for x in nums]
        counter = 0
        def isolated(i, j):
            visited[i][j] = True
            if not (i == 0 or nums[i-1][j] == "0" or visited[i-1][j] == True):
                isolated(i-1, j)
            if not(j == 0 or nums[i][j-1] == "0" or visited[i][j-1] == True):
                isolated(i, j-1)
            if not(i == len(nums)-1 or nums[i+1][j] == "0" or visited[i+1][j] == True):
                isolated(i+1, j)
            if not (j == len(nums[0])-1 or nums[i][j+1] == "0" or visited[i][j+1] == True):
                isolated(i, j+1)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] == "1" and not visited[i][j]: 
                    isolated(i,j)
                    counter +=1
        return counter
        
