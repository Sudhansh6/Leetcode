class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not len(s):
            return 0
        g.sort()
        s.sort()
        j = 0
        count = 0
        for i in range(len(s)):
            if g[j] <= s[i]:
                count += 1
                j += 1
            if j == len(g):
                break
        return count
            