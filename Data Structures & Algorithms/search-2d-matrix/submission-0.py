class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                return self.bst_row(matrix[m], target)
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                r = m - 1

        return False

    def bst_row(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2

            if target == row[m]: 
                return True 
            elif target > row[m]:
                l = m + 1
            else:
                r = m - 1

        return False