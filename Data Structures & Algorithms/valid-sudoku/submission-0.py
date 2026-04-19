class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = 9

        for row in range(n):
            seen = set()
            for col in range(n):
                cell = board[row][col]
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
        
        for col in range(n):
            seen = set()
            for row in range(n):
                cell = board[row][col]
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
        
        for row in range(n//3):
            for col in range(n//3):
                seen = set()

                for sub_row in range(n//3):
                    for sub_col in range(n//3):
                        cell = board[sub_row + row * 3][sub_col + col * 3]
                        
                        if cell != '.' and cell in seen:
                            return False
                        
                        seen.add(cell)
                

        return True
