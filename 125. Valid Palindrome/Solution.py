class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Step 1: Convert to lowercase
        s = s.lower()

        # Step 2: Initialize two pointers
        left, right = 0, len(s) - 1

        # Step 3: Loop until pointers meet
        while left < right:
            # Ignore non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1  # Move left pointer forward
            while left < right and not s[right].isalnum():
                right -= 1  # Move right pointer backward

            # Compare letters from both ends
            if s[left] != s[right]:
                return False  # Not a palindrome
            
            # Move pointers inward
            left += 1
            right -= 1
        
        return True  # It's a palindrome!
