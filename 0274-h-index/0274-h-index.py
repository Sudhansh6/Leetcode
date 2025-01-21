class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            return int(citations[0] > 0)

        citations.sort()
        
        # Binary search
        l, r = 0, len(citations)
        while r - l > 1:
            m = (r + l)//2
            if citations[m] >= len(citations) - m:
                r = m
            else:
                l = m
        
        if citations[l] >= len(citations) - l:
            return len(citations) - l
        return len(citations) - r