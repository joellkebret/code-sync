class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check rows 
        for row in board:
            seen = set()
            for num in row:
                if num == '.':
                    continue
                
                if num in seen:
                    return False
                
                seen.add(num)
        
        # Column Check
        for col in range(9): 
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                
                if board[row][col] in seen:
                    return False
                
                seen.add(board[row][col])

        # Sub Box Check
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[row +i][col +j] == '.':
                            continue
                        
                        if board [row + i][col +j] in seen:
                            return False
                        
                        seen.add(board[row +i][col +j])
        return True # All conditions pass