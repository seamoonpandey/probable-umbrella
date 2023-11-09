class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Create instance of the Solution class
solution = Solution()

s = input("Enter the first string")
t = input("Enter the second string")

print(solution.isAnagram(s,t))