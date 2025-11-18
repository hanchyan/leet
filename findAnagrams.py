class Solution:
    def findAnagrams(self, s: str, p: str):
        preList = []
        for i in range(len(s)):
            if s[i] in p:
                preList.append(i)

        print(preList)

if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    Solution().findAnagrams(s,p)
        
