class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            row_set = set() 
            for el in row:
                if el == ".":
                    continue
                elif el in row_set:
                    return False
                else:
                    row_set.add(el)

        # check cols 
        for i in range(len(board[0])):
            col_set = set()
            for j in range(len(board)):
                el = board[j][i]
                if el == ".":
                    continue
                elif el in col_set:
                    return False
                else:
                    col_set.add(el)

        # check boxes
        # integer division by 3 --> determine 3x3 box
        # entry = (row, col) tuple (check for dups)
        box_set = collections.defaultdict(set) 
        for i in range(len(board)):

            for j in range(len(board[i])):
                el = board[i][j]
                tup = (i//3, j//3)
                if el == ".":
                    continue
                elif el in box_set[tup]:
                    return False
                else:
                    box_set[tup].add(el)

        return True