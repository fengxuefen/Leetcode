'''
Created on 2015-11-03

@author: Fen
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 : 
            return False
        div = 1
        while( x / div >= 10) :
            div = div * 10
        while(x != 0):
            if( x / div != x % 10) :
                return False
            x = x % div / 10
            div = div / 100
        return True