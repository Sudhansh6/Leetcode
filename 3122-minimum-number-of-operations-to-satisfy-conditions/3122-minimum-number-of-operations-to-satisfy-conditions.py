class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        # for each column store the unique elements
        m, n = len(grid), len(grid[0])

        choices = [dict() for i in range(n)]
        for i in range(m):
            for j in range(n):
                choices[j][grid[i][j]] = choices[j].get(grid[i][j], 0) + 1
        
        print(choices)
        # DP
        dp = {}
        def helper(prev, i):
            res = m * n
            if i == n:
                return 0

            if dp.get((prev, i), -1) > 0:
                return dp[(prev, i)] 

            for k, v in choices[i].items():
                if k == prev:
                    res = min(res, helper(-prev - 1, i + 1) + m)
                else:
                    res = min(res, helper(k, i + 1) + m - v)

            dp[(prev, i)] = res
            return res
        
        return helper(-1, 0)