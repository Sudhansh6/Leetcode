class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [i + 1 for i in range(n)]
        res.sort(key=lambda c: str(c))
        return res
            