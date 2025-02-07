class Solution:
    def minSwaps(self, s: str) -> int:
        if len(s) == 1:
            return 0

        num_zeros = 0
        for i in range(len(s)):
            if s[i] =="0":
                num_zeros += 1
        num_ones = len(s) - num_zeros 

        if abs(num_ones - num_zeros) > 1:
            return -1
        
        res1 = 0
        res2 = 0

        if num_ones > num_zeros:
            res2 = len(s)
        elif num_ones < num_zeros:
            res1 = len(s)

        flag1 = False
        flag2 = False
        for i in range(len(s)):
            if num_ones >= num_zeros:
                flag1 = int(s[i]) == i % 2
            if num_ones <= num_zeros:
                flag2 = int(s[i]) != i % 2
            
            if flag1:
                res1 += 1
            if flag2:
                res2 += 1
        
        return min(res1, res2)//2
            