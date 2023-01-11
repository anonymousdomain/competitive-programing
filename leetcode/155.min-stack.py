#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        
        self.s1=[]
    
        
    def push(self, val: int) -> None:
        self.s1.append(val)

    def pop(self) -> None:
        if len(self.s1)>0:
             self.s1.pop()

    def top(self) -> int:
        if self.s1:
            return self.s1[-1]

    def getMin(self) -> int:
        return  min(self.s1) 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

