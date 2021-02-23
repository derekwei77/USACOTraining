# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: string
        :rtype: bool
        """
        s1 = []
        for letter in s:
            if letter.isalnum():
                s1.append(str(letter).lower())
        start = 0
        end = len(s1) - 1
        palindrome = True
        while (start < end):
            if (s1[start] != s1[end]):
                palindrome = False
                break
            start += 1
            end -= 1
        return palindrome

solution = Solution()
s = 'HeH'
print(solution.isPalindrome(s))

s = 'Hell'
print(solution.isPalindrome(s))

s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))

s = "race a car"
print(solution.isPalindrome(s))

s = ''
print(solution.isPalindrome(s))