class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = {}
        left = 0
        max_so_far = 0
        for i in range(len(s)):
            if checker.get(s[i], -1) >= left:
                max_so_far = max(max_so_far, i - left)
                left = checker.get(s[i], -1) + 1
            checker[s[i]] = i
        max_so_far = max(max_so_far, len(s) - left)
        return max_so_far