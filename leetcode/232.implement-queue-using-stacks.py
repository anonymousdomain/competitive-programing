#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
      
        
    def push(self, x: int) -> None:
        
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        
        self.stack_in.append(x)
        
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())

    def pop(self) -> int:
        return self.stack_in.pop()
    def peek(self) -> int:
        
        return self.stack_in[-1]
        
    def empty(self) -> bool:
       return len(self.stack_in)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push([[],[1],[2],[],[],[]])
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# print(obj.stack_in)

# @lc code=end

