'''
Created on 2015-11-02

@author: Fen
'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        medianV = indexM = indexN = 0;
        k = (m + n) / 2
        k = k + 1
        for index in range(k) :
            if(index == k - 1 or (index == k - 2 and (m + n) % 2 == 0)) :
                if(indexN == n) :
                    medianV = medianV + nums1[indexM]
                    indexM = indexM + 1
                elif(indexM == m):
                    medianV = medianV + nums2[indexN]
                    indexN = indexN + 1
                else :
                    if(nums1[indexM] < nums2[indexN]) :
                        medianV = medianV + nums1[indexM]
                        indexM = indexM + 1
                    else :
                        medianV = medianV + nums2[indexN]
                        indexN = indexN + 1
            else:
                if(indexN == n) :
                    indexM = indexM + 1
                elif(indexM == m):
                    indexN = indexN + 1
                else :
                    if(nums1[indexM] < nums2[indexN]) :
                        indexM = indexM + 1
                    else :
                        indexN = indexN + 1
        if((m + n) % 2 == 0 and m + n > 1) :
            medianV = float(medianV) / 2
        return medianV