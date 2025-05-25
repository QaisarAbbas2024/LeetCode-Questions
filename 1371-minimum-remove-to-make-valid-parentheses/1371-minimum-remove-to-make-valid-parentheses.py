class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        # Step 1: Initialize stack to keep track of unmatched '(' positions.
        stack = []
        s = list(s)  # Convert string to list so we can modify it in-place

        # Step 2: First pass - remove unmatched closing parentheses ')'
        for i in range(len(s)):
            if s[i] == '(':
                # If it's '(', store its index to match later
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    # Found a matching '(', pop it from the stack
                    stack.pop()
                else:
                    # Unmatched ')', mark it for removal
                    s[i] = ''

        # Step 3: Second pass - remove any unmatched opening parentheses '('
        while stack:
            # Set unmatched '(' to empty string using its index
            s[stack.pop()] = ''

        # Join and return the valid string
        return ''.join(s)
