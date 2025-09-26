class Solution:
    def eatingTime(self,k,piles):
        t=0
        for pile in piles:
            t+=(pile+k-1)//k
        return t
    def minEatingSpeed(self, piles, h):
        piles.sort()
        length=len(piles)
        left=0
        right=piles[length-1]
        while left<=right:
            mid=(left+right)//2
            t=self.eatingTime(mid,piles)
            #print(t,mid,left,right)
            if t>h:
                left=mid+1
            if t<=h:
                if mid==1:
                    return mid
                if mid>1 and self.eatingTime(mid-1,piles)>h:
                    return mid
                right=mid-1
        #return mid
s=Solution()
print(s.minEatingSpeed([312884470],968709470))