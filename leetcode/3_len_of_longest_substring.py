# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp_str = ""
        for i in s:
            if i not in temp_str:
                temp_str += i
            if temp_str not in s:
                temp_str = temp_str[1:]
        return len(temp_str)


if __name__ == '__main__':
    # str = "abcabcbb"
    str = "pwwkew"
    s = Solution()
    print(s.lengthOfLongestSubstring(str))
