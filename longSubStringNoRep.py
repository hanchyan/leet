class Solution(object):
    def lengthOfLongestSubstring(self, s):
        print(len(s))

        return 0

if __name__ == "__main__":
    s = "abcabcbb"
    print("Length of Longest Substring:", Solution().lengthOfLongestSubstring(s))



# it would be like put a character from the string in an array
# put the next character in the array if it does not already exist in the array 
# if it already exists, dont add it, get the length of the array and compare it to the current max 
# length and update the max length variable... 
