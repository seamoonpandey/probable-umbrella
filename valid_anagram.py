class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable = set()
        for c in s:
            hashtable.add(c)
        for c in t:
            if c not in hashtable:
                return False
        return True

# Create instance of the Solution class
solution = Solution()

s = input("Enter the first string")
t = input("Enter the second string")

print(solution.isAnagram(s,t))