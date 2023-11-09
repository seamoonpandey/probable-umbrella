class Solution:
    def containDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False

# Create an instance of the Solution class
solution = Solution()

# Test the containDuplicate method with a list of integers
nums = [1, 2, 3, 4, 5]
result = solution.containDuplicate(nums)
if result:
    print("There are duplicate elements in the list.")
else:
    print("There are no duplicate elements in the list.")