class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Step 1: Convert binary to decimal
        num1 = int(a, 2)  # Convert 'a' to decimal
        num2 = int(b, 2)  # Convert 'b' to decimal
        
        # Step 2: Add the numbers
        total = num1 + num2  # Normal addition in decimal
        
        # Step 3: Convert back to binary and return (removing '0b' prefix)
        return bin(total)[2:]  # bin() gives '0b...' so we remove '0b'
