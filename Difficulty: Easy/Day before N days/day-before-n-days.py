class Solution:
    def findAnswer(self, d, n): 
        x=n%7
        z=d-x
        if z>=0:
            return z
        else:
            return z+7
