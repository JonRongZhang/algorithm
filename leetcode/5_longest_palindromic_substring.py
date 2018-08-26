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
    def longestPalindrome(self, s):  # Brute Force
        """
        :type s: str
        :rtype: str
        """
	result = str()
	max_len = 0

        for i in range(len(s) + 1):
	    for j in range(i + 1, len(s) + 1):
	    	test_sub = s[i:j]
		if self._is_palindrome(test_sub) and len(test_sub) > max_len:
		    result = test_sub
		    max_len = len(test_sub)

	return result


    @staticmethod
    def _is_palindrome(s):
        i = len(s) - 1
	j = 0
	while i > j:
	    if s[i] != s[j]:
	        return False
	    i -= 1
	    j += 1
	return True


    def longest_palindrome_1(self, s):  # Dynamic Programming
	reverse_str = s[::-1]
	array= [[0 for x in range(len(s))] for y in range(len(s))]
	max_len = max_end = 0

	for i in range(len(s)):
	    for j in range(len(s)):
	        if s[i] == reverse_str[j]:
		    if i == 0 or j == 0:
		        array[i][j] = 1
	            else:
		        array[i][j] = array[i-1][j-1] + 1

		if array[i][j] > max_len:
		    before = len(s) - 1 - j
		    if before + array[i][j] - 1 == i:
		        max_len = array[i][j]
		        max_end = i
	#print(array)
	#print(reverse_str)
	#print(max_len, max_end)
	return s[max_end - max_len + 1:max_end + 1]


    def longest_palindrome_2(self, s):
        pass


if __name__ == "__main__":
    s = Solution()
    #i = "babad"
    #i = "cbbd"
    #i = "abccb"
    #i = "abc435cba"
    i = "abacdfgdcaba"
    print(s.longestPalindrome(i))
    print(s.longest_palindrome_1(i))

