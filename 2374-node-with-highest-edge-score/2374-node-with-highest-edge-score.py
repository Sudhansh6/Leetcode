class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        res = [0]*len(edges)
        for u, v in enumerate(edges):
            res[v] += u
        
        mi = 0
        for i in range(len(edges)):
            if res[i] > res[mi]:
                mi = i
        return mi