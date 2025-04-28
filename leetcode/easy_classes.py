'''
Problem: https://leetcode.com/problems/merge-two-sorted-lists/
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Problem: https://leetcode.com/problems/min-stack/
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    '''
    This might look incorrect at first, but it's actually very clever.
    Since in a stack we'll be removing one by one the last element added to the list (LIFO) we can add the same min value
    each time we add a new element to the stack, while the current min value is lower than the newly added value.
    Ex: stack = [1, 2, 3] minStack = [1, 1, 1] pop => stack = [1, 2] minStack = [1, 1]
    '''
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1],val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    # Your MinStack object will be instantiated and called as such:
    # obj = MinStack()
    # obj.push(val)
    # obj.pop()
    # param_3 = obj.top()
    # param_4 = obj.getMin()

'''
Problem: https://leetcode.com/problems/implement-queue-using-stacks/
'''
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.isEmpty = True

    def push(self, x: int) -> None:
        '''
        To implement a queue using two stacks we need to focus on add operation,
        popping all elements in our correctly ordered stack and adding them to a second one will let us
        add the new value at the end of the queue, after that we pop from the second stack
        to add it to the original stack.
        Remember Stack implements LIFO while a Queue implements FIFO.
        '''
        stack2 = []
        if self.isEmpty:
            self.stack1.append(x)
            self.isEmpty = False
        else:
            lenStack = len(self.stack1)
            while lenStack > 0:
                lenStack -= 1
                stack2.append(self.stack1.pop())
            stack2.append(x)
            lenStack = len(stack2)
            while lenStack > 0:
                lenStack -= 1
                self.stack1.append(stack2.pop())
        

    def pop(self) -> int:
        if self.isEmpty: return None
        if len(self.stack1) == 1: self.isEmpty = True
        return self.stack1.pop()

    def peek(self) -> int:
        if self.isEmpty: return None
        x = self.stack1.pop()
        self.stack1.append(x)
        return x

    def empty(self) -> bool:
        return self.isEmpty
        
    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    # param_4 = obj.empty()


obj = MyQueue()
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_4)

obj = MinStack()
obj.push(1)
obj.push(2)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)