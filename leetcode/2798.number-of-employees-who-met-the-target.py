#
# @lc app=leetcode id=2798 lang=python3
#
# [2798] Number of Employees Who Met the Target
#

# @lc code=start
from typing import List
import unittest

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        output=[]
        for hour in hours:
            if hour>=target:
                output.append(hour)
        
                
        return len(output)
        
# @lc code=end
class TestNumberOfEmployeesWhoMetTarget(unittest.TestCase):
        def test_number_of_employees_met_target(self):
          self.assertEqual(Solution.numberOfEmployeesWhoMetTarget(self=Solution,hours=[0,1,2,3,4],target=2),3)  
          self.assertEqual(Solution.numberOfEmployeesWhoMetTarget(self=Solution,hours=[5,1,4,2,2],target=6),0)  
          
if __name__ == '__main__':
    unittest.main()