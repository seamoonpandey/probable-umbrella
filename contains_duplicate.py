class Solution:
    def containDuplicate(self, nums) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False

# Create an instance of the Solution class
solution = Solution()

input_str = input("Enter a list of integers separated by commas: ")

# Convert the input string into a list of integers
nums = [int(x) for x in input_str.split(',')]

print(solution.containDuplicate(nums))