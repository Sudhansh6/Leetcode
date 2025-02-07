class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        res = self.validStrings(n - 1)
        l = len(res)
        for i in range(l):
            if res[i][0] != "0":
                res.append("0" + res[i])
            res[i] = "1" + res[i]
        return res