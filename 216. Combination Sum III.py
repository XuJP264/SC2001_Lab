class Solution:
    def findMax(self,n,note,queue):
        for i in range(9,0,-1):
            if i<=n and note[i]==False and i<queue[-1]:
                return i
        return -1
    def insert(self,k,n,note,queue):
        if k==0 or n<=0:
            return False
        else:
            if queue:
                valid_max=self.findMax(n,note,queue)
                if valid_max>0:
                    queue.append(valid_max)
                    k -= 1
                    n -= valid_max
                    note[valid_max] = True
                else:
                    return False
            else:
                if n>9:
                    queue.append(9)
                    k-=1
                    n-=9
                    note[9]=True
                else:
                    queue.append(n)
                    k -= 1
                    n -= n
                    note[n] = True
                return True

    def fix(self,k,n,note,queue):
        if k==0 and n>0:
            return False
        if k>0 and n==0:
            for i in range(len(queue)-1,-1,-1):
                if queue[i]>1:


        if k==0 and n==0:

    def combinationSum3(self, k, n):
        results=[]
        quque=[]
        k_current=k
        n_current=n
        note=[False for _ in range(1,10)]
        while :
            if k_current==0 and n_current==0:
                results.append(quque)
            if self.insert(n_current,note,k_current,quque):
            elif self.fix(n_current,note,k_current,quque):
            else:
                break
