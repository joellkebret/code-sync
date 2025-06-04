class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get dimensions of the matrix 
        rows = len(matrix)
        cols = len(matrix[0])

        # let low be first row, and high be last
        low = 0
        high = rows*cols-1

        while low <= high:
            mid = (low+high)//2 # middle row
            # This step allows us to view the matrix almost as a giant list
            # row = mid//cols find the middle row
            # col = mid % cols the column we should move to based on position
            row,col = mid//cols, mid%cols 
            guess = matrix[row][col]

            if guess == target:
                return True
            
            elif guess > target:
                high = mid -1
            
            else:
                low = mid + 1
        
        return False