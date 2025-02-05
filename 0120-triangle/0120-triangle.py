class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        # Have to do backtracking, no other choice
        def helper(arrs, i, j):
            if dp.get((i, j), None) != None:
                return dp[(i, j)]
            if i == len(arrs) - 1:
                return arrs[i][j]
            res = arrs[i][j] + helper(arrs, i + 1, j)
            if j < len(arrs[i]):
                res2 = arrs[i][j] + helper(arrs, i + 1, j + 1)
                if res2 < res:
                    res = res2
            dp[(i, j)] = res
            return res
        
        return helper(triangle, 0, 0)

        