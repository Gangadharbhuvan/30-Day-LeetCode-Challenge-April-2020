'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.



'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__a = []

    def push(self, x: int) -> None:
        m = x
        if self.__a:
            m = self.__a[-1][1]
            if m > x:
                m = x
        self.__a.append((x, m))

    def pop(self) -> None:
        self.__a.pop()
        
    def top(self) -> int:
        return self.__a[-1][0]

   
    def getMin(self) -> int:
        return self.__a[-1][1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
