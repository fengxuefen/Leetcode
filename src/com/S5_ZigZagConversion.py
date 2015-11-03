'''
Created on 2015-11-03

@author: Fen
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1) :
            return s;
        resultString = ""
        for rows in range(numRows) :
            index = rows
            judgeodd = True
            if rows + 1 > len(s) :
                return resultString
            resultString = resultString + s[index]
            while(True) :
                if judgeodd and (numRows - rows - 1 != 0) :
                    index = index + (numRows - rows - 1) * 2
                    if(index >= len(s)) :
                        break;
                    resultString = resultString + s[index]
                elif not judgeodd and (rows != 0) :
                    index = index + rows * 2
                    if(index >= len(s)) :
                        break;
                    resultString = resultString + s[index]
                judgeodd = not judgeodd
        return resultString

            