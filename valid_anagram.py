class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s)!=len(t):
        #     return False
        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # for c in countS:
        #     if countS[c] != countT.get(c,0):
        #         return False
        # return True
        return Counter(s) == Counter(t)

        # return sorted(s) == sorted(t)

# Create instance of the Solution class
solution = Solution()

s = input("Enter the first string")
t = input("Enter the second string")

print(solution.isAnagram(s,t))