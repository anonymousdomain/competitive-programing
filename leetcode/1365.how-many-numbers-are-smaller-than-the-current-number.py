
from typing import List
import unittest

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter=0
        arr=[]
        for i in range(0,len(nums)):
            current_number=nums[i]
            for ls in nums:
                if ls<current_number:
                    counter+=1
            arr.append(counter)
            print(counter)
            counter=0
        return arr
class TestNumbersSmallerThanCurrentNumbers(unittest.TestCase):
    
    def test_nums(self):
        st=Solution.smallerNumbersThanCurrent(self=Solution,nums=[8,1,2,2,3])
        self.assertEqual(st,[4,0,1,1,3])

if __name__=='__main__':
    unittest.main()
