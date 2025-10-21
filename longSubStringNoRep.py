class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = []  # list to store current substring
        long_sub = 0
        new_sub = 0
        for i in s:
            if i not in sub:
                sub.append(i)
                new_sub = len(sub)
                long_sub = max(new_sub, long_sub)
            # else:
            #     print("it was already there")
        print(long_sub)
        
        return 0  # placeholder

if __name__ == "__main__":
    s = "abcafbcbb"
    Solution().lengthOfLongestSubstring(s)




#it would be like put a character from the string in an array
#put the next character in the array if it does not already exist in the array 
#if it already exists, dont add it, get the length of the array and compare it to the current max 
#length and update the max length variable... 


	
