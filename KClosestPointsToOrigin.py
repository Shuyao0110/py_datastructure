class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        result=[]
        right=self.findUpperClosest(arr,x)
        left=right-1
        for i in range(k):
            if self.isLeftCloser(arr,x,left,right):
                result.append(arr[left])
                left-=1
            else:
                result.append(arr[right])
                right+=1
        return sorted(result)

    def findUpperClosest(self,arr,x):
        start,end =0,len(arr)-1
        while start+1<end:
            mid=(start+end)/2
            if arr[mid]<x:
                start=mid
            else:
                end=mid
        return end
        
    def isLeftCloser(self,arr,x,left,right):
        if left<0:
            return False
        if right>=len(arr):
            return True
        if x-arr[left]<=arr[right]-x:
            return True
    
        