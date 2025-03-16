class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
    # Step 1: Create an empty dictionary to store letter counts
        letter_count = {}

    # Step 2: Count letters in magazine
        for letter in magazine:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    # Step 3: Check if we can build ransomNote
        for letter in ransomNote:
            if letter in letter_count and letter_count[letter] > 0:
                letter_count[letter] -= 1  # Use one letter
            else:
                return False  # Not enough letters

        return True
   
