class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False  # If lengths are different, they can't be anagrams
        
        char_count = {}  # Dictionary to store character frequency
        
        # Count frequency of characters in string 's'
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Reduce the frequency based on string 't'
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] == 0:
                    del char_count[char]  # Remove if count reaches zero
            else:
                return False  # If character is not in 's', return False
        
        return len(char_count) == 0  # If dictionary is empty, it's an anagram
