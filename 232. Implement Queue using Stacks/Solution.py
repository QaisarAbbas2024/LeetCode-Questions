class MyQueue(object):

    def __init__(self):
        self.stack1 = []  # Used for push operations
        self.stack2 = []  # Used for pop/peek operations

    def push(self, x):
        """
        Pushes element x to the back of the queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)  # Standard push operation

    def pop(self):
        """
        Removes and returns the element from the front of the queue.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Move elements from stack1 to stack2
        return self.stack2.pop()  # Standard pop operation

    def peek(self):
        """
        Returns the element at the front of the queue.
        :rtype: int
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())  # Move elements if stack2 is empty
        return self.stack2[-1]  # Peek at the top of stack2 (front of queue)

    def empty(self):
        """
        Returns true if the queue is empty, false otherwise.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2  # Queue is empty if both stacks are empty
