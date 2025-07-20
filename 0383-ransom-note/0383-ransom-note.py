class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        #Step 1: Create An empty dictionary
        letter_count = {}

        #Step 2: Count letters in magazine
        for letter in magazine:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
       

        #Step 3: Check if we can build ransomnote
        for letter in ransomNote:
            if letter in letter_count and letter_count[letter] > 0:
                letter_count[letter] -= 1
            else:
                return False
        return True

        