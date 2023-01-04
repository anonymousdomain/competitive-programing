import unittest
def countingValleys(steps, path):
    # Write your code here
    count=0
    mountain=0
    for i in range(steps):
        if path[i]=='U':
           count+=1
        else: 
           count-=1
        if count==0 and path[i]=='U':
            mountain+=1
    return mountain

class TestCountinVally(unittest.TestCase):
    
    def test_counting_setps(self):
        result=countingValleys(8,'UDDDUDUU')
        self.assertEqual(result,1)
        
        
    


if __name__=='__main__':
    
    unittest.main()