class Solution:
    

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        }

        res =  mapping[digits[0]].copy()
        for i in range(1, len(digits)):
            l = len(res)
            for j in range(l):
                for c in mapping[digits[i]][1:]:
                    res.append(res[j] + c)
                res[j] += mapping[digits[i]][0]
        return res