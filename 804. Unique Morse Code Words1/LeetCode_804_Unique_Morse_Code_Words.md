
# LeetCode 804: Unique Morse Code Words

## 🧩 Problem Statement

Given an array of strings `words`, return the number of **different** Morse code representations made by words in the list.

Each letter of the alphabet is mapped to a Morse code string as follows:

```
a -> ".-"
b -> "-..."
c -> "-.-."
...
z -> "--.."
```

---

## 🧪 Examples

### Example 1:
**Input**:  
`words = ["gin", "zen", "gig", "msg"]`  
**Output**:  
`2`  
**Explanation**:  
- "gin" -> `"--...-."`
- "zen" -> `"--...-."`
- "gig" -> `"--..--."`
- "msg" -> `"--..--."`

There are only **2 unique** Morse representations.

---

## ✅ Python Solution

```python
class Solution:
    def uniqueMorseRepresentations(self, words):
        # Morse codes for letters a to z
        morse_codes = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        
        # Set to store unique Morse transformations
        transformations = set()
        
        # For each word in the input list
        for word in words:
            morse_word = ""
            for char in word:
                # Convert character to index (ord('a') = 97)
                index = ord(char) - ord('a')
                morse_word += morse_codes[index]
            
            # Add the transformed Morse word to the set
            transformations.add(morse_word)
        
        # Return number of unique transformations
        return len(transformations)
```

---

## 🧠 Line-by-Line Explanation

- **`morse_codes`**: A list of 26 Morse code strings for 'a' to 'z'.
- **`transformations`**: A set to keep unique Morse representations.
- **Loop through each word**:
  - Convert it to Morse using character indices.
  - Add the Morse string to the set.
- **Return** the number of unique elements in the set.

---

## 📝 Summary

- Time Complexity: **O(n * k)**  
  where `n` = number of words, `k` = average word length.
- Space Complexity: **O(n)** for storing Morse codes in the set.
