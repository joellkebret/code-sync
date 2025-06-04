class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique = set()
        nums.sort()

        for i in range(len(nums)):
            # Skip duplicates for the fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    trip = (nums[i], nums[l], nums[r])
                    unique.add(trip)

                    # Skip duplicates after a match
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return [list(t) for t in unique]