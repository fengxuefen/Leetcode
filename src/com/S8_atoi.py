'''
Created on 2015-11-03

@author: Fen
'''
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip();
        if(len(str) == 0) :
            return 0;
        numstr = str[0]
        result = 0
        if(str[0] != '+' and str[0] != '-' and (str[0] > '9' or str[0] < '0')) :
            return result;
        for x in str[1:]:
            if(x > '9' or x < '0') :
                break;
            else:
                numstr = numstr + x;
        if len(numstr) > 1 or numstr.isdigit() :
            number = int(numstr)
            if(number > 2147483647) :
                return 2147483647
            elif(number < -2147483648) :
                return -2147483648
            return number
        else :
            return 0
        