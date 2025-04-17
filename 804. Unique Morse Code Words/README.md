
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

---

## 🧠 Line-by-Line Explanation (Extended)

class Solution:
We’re creating a class named Solution. This is required because LeetCode expects a method inside a class.

def uniqueMorseRepresentations(self, words):
This defines a function called uniqueMorseRepresentations, which:

Takes two arguments:

self → refers to the object of the class.

words → a list of lowercase strings like ["gin", "zen", "gig"].

morse_codes = [...]
This is a list of Morse code strings.
Each position in the list represents the Morse code for a letter:

morse_codes[0] is .− → for a

morse_codes[1] is −... → for b

...

morse_codes[25] is --.. → for z

So we can convert a character to its Morse code using its position in the alphabet.

transformations = set()
This creates an empty set to store all the Morse code versions of the words.
Why a set?
Because a set automatically removes duplicates – so we can easily count unique ones.

for word in words:
Now we loop through each word in the list words.

morse_word = ""
We start with an empty string to build the Morse version of the current word.

for char in word:
For each letter (char) in the word, we’ll find its Morse equivalent.

index = ord(char) - ord('a')
We convert the letter into an index:

ord('a') gives 97.

So ord('b') - ord('a') → 98 - 97 = 1, which points to morse_codes[1].

This gives us a fast way to map letters to Morse code.

morse_word += morse_codes[index]
We add the Morse code of each character to morse_word.

transformations.add(morse_word)
After we’ve built the Morse version of a word, we add it to the set of transformations.

Even if it's already in the set, duplicates are ignored.

return len(transformations)
Finally, we return the count of unique Morse codes by checking the length of the set.

🧾 Example Walkthrough
Input:

python
Copy
Edit
["gin", "zen", "gig", "msg"]
"gin" → "--...-."

"zen" → "--...-." (same as "gin")

"gig" → "--..--."

"msg" → "--..--." (same as "gig")

Set only keeps:

python
Copy
Edit
{"--...-.", "--..--."}
So, 2 unique transformations → return 2

---
