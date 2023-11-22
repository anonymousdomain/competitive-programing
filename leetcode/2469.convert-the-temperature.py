
# @lc app=leetcode id=2469 lang=python3
#
# [2469] Convert the Temperature
#

# @lc code=start
from typing import List
import unittest

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        
        return [Kelvin,Fahrenheit]
        
# @lc code=end

class TestConvertTemprature(unittest.TestCase):
    
    def test_convert_temprature(self):
        self.assertEqual(Solution.convertTemperature(self=Solution,celsius=36.50),[309.65000,97.70000])
        
if __name__ == '__main__':
    unittest.main()