class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = 0
        
        for num in nums:
            if jumps<0:
                return False
            
            elif num>jumps:
                jumps = num
            
            jumps-=1
        
        return True