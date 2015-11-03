'''
Created on 2015-11-03

@author: Fen
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        nagative = False
        if x < 0 :
            nagative = True
        x = abs(x)
        while(x >= 1) :
            result = result * 10 + x % 10
            x = x / 10
        if(abs(result) > 2**31 - 1) :
            return 0
        if nagative :
            result = -result
        return result