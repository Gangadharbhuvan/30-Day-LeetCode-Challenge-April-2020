'''
	Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

'''


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S, T = self._helper(S), self._helper(T)
        return S == T
    
    def _helper(self,s):
        while "#" in s:
            i = s.index("#")
            s = s[:i-1] + s[i+1:] if i > 0 else s[i+1:]
        return s
