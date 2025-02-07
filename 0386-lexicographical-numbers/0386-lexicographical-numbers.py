class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [0 for _ in range(n)]
        curr = 1
        for i in range(n):
            res[i] = curr
            if curr * 10 <= n:
                curr *= 10
                continue
            else:
                while curr % 10 == 9 or curr >= n:
                    curr //= 10
                curr += 1
        return res
            
            