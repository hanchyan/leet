class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        sub = []  # list to store current substring
        long_sub_len = 0
        new_sub_len = 0
        while i < len(s):
            char = s[i]
            if char not in sub:
                sub.append(char)
                new_sub_len = len(sub)
                long_sub_len = max(new_sub_len, long_sub_len)
                print (long_sub_len)
                i += 1
            else:
                # sub.clear()
                print("char clear" +" " +char)
                first_instance_char = sub.index(char)
                sub = sub[first_instance_char+1:]  # keep only elements after the first occurrence
                # i = i -1
                sub.append(char)
                i += 1

        print(long_sub_len)
        return long_sub_len  # placeholder

if __name__ == "__main__":
    s = "pwwkew"
    # s = "qrstuvwxxabcdefghiijklmnopqrstuv"
    Solution().lengthOfLongestSubstring(s)
