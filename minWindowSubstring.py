class Solution(object):
    def minWindow(self, s, t):
        sub = []
        for char in s:
            if char in t:
                sub.append(char)
                print(sub)


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "qrstuvwxxabcdefghiijklmnopqrstuv"
    Solution().minWindow(s,t)
