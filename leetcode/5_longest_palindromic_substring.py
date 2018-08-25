# Difficulty: Medium
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example 2:
#
# Input: "cbbd"
# Output: "bb"



class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_dict = dict()
        max_letter = s[0]

        for i in range(len(s)):
            if s[i] not in temp_dict:
                temp_dict[s[i]] = [0]
            temp_dict[s[i]][0] += 1
            temp_dict[s[i]].append(i)

            if i > 1 and temp_dict[s[i]][0] > temp_dict[max_letter][0]:
                max_letter = s[i]

        #print(temp_dict)
        #print(max_letter)
        #print(temp_dict[max_letter])
        return s[temp_dict[max_letter][1]:temp_dict[max_letter][-1] + 1]


if __name__ == "__main__":
    s = Solution()
    #i = "babad"
    i = "cbbd"
    print(s.longestPalindrome(i))
