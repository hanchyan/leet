class Solution(object):
    def lengthOfLongestSubstring(self, s):
        sub = []  # list to store current substring
        long_sub_len = 0
        new_sub_len = 0
        for i in s:
            if i not in sub:
                sub.append(i)
                new_sub_len = len(sub)
                long_sub_len = max(new_sub_len, long_sub_len)
                # print(long_sub_len)
            else:
                sub.clear()
                print("all clear")
        print(long_sub_len)
        
        return long_sub_len  # placeholder

if __name__ == "__main__":
    s = "aab"
    # s = "qrstuvwxxabcdefghiijklmnopqrstuv"
    Solution().lengthOfLongestSubstring(s)


#it would be like put a character from the string in an array
#put the next character in the array if it does not already exist in the array 
#if it already exists, dont add it, get the length of the array and compare it to the current max 
#length and update the max length variable... 


	
