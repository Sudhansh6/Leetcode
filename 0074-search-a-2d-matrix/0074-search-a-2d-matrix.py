class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search row
        l, r = 0, len(matrix)
        mid = (l + r)//2
        while (r - l) > 1:
            if matrix[mid][0] > target:
                r = mid
            elif matrix[mid][0] < target:
                l = mid
            else:
                return True
            mid = (l + r)//2

        if r < len(matrix) and matrix[r][0] < target:
            mid = r 

        l, r = 0, len(matrix[mid])
        mid2 = (l + r)//2
        while (r - l) > 1:
            if matrix[mid][mid2] > target:
                r = mid2
            elif matrix[mid][mid2] < target:
                l = mid2
            else:
                return True
            mid2 = (l + r)//2

        if r < len(matrix[mid]) and matrix[mid][r] == target:
            return True
        if matrix[mid][mid2] == target:
            return True 
            
        return False