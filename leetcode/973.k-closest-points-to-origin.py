 #
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from typing import List
import unittest
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sqr=[]
        for i in range(0,len(points)):
            x=points[i][0]
            y=points[i][1]
            distance=math.sqrt(x**2+y**2)
            heapq.heappush(sqr,(distance,x,y))
            min_distance=[]
        
        for i in range(k):
            d,x,y=heapq.heappop(sqr)
            min_distance.append([x,y])
        return min_distance
       
        
            
# @lc code=end


class TestKClosestPoint(unittest.TestCase):
    def test_kclose(self):
        s=Solution.kClosest(self=Solution,points=[[1,3],[-2,2]],k=1)
        self.assertEqual(s,[[-2,2]])

if __name__=='__main__':
    unittest.main()
