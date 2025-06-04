class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = {}

        for i in range(len(arr)):
            #seen
            if arr[i] in counts:
                counts[arr[i]] +=1
                if counts[num] > len(arr)/4:
                    return num
            else:
                # new
                counts[arr[i]] = 1
        
        for num in counts:
            if counts[num] > len(arr)/4:
                return num