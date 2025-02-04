class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maximum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 0:
                    continue

                if i > 0 and j > 0:
                    matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                # print(i, j, matrix[i][j])
                maximum = max(maximum, matrix[i][j])
                
        return maximum*maximum