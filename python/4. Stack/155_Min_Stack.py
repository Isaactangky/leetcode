# use (val, curmin) stack
# when adding new val, new min = min(min of last element, val)
# O(1) time for retriving min, popping, pushing and top

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
        else:
            curMin = min(val, self.stack[-1][1])
            self.stack.append((val, curMin))
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 
        else:
            return self.stack[-1][0]
    def getMin(self) -> int:
        if len(self.stack) == 0:
            return 
        else:
            return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
