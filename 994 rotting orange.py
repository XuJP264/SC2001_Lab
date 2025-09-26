class Solution:
    def __init__(self):
        self.o_num=0
    def rotten(self,cur,or_map,visits,q):
        index=cur[0]
        if or_map.get((index[0]+1,index[1])) == 1 and visits.get((index[0]+1,index[1])) == False:
            self.o_num -= 1
            or_map[(index[0] + 1, index[1])] = 2
            q.append([(index[0]+1,index[1]),cur[1]+1])
            #visits[(index[0]+1,index[1])]=True
        if or_map.get((index[0]-1,index[1])) == 1 and visits.get((index[0]-1,index[1])) == False and index[0]>0:
            self.o_num -= 1
            or_map[(index[0] - 1, index[1])] = 2
            q.append([(index[0]-1,index[1]),cur[1]+1])
            #visits[(index[0]-1,index[1])]=True
        if or_map.get((index[0],index[1]+1)) == 1 and visits.get((index[0],index[1]+1)) == False:
            self.o_num -= 1
            or_map[(index[0], index[1] + 1)] = 2
            q.append([(index[0],index[1]+1),cur[1]+1])
            #visits[(index[0]-1,index[1])]=True
        if or_map.get((index[0],index[1]-1)) == 1 and visits.get((index[0],index[1]-1)) == False and index[1]>0:
            self.o_num -= 1
            or_map[(index[0], index[1] - 1)] = 2
            q.append([(index[0],index[1]-1),cur[1]+1])
            #visits[(index[0]-1,index[1])]=True
        if self.o_num==0:
            return cur[1]+1
        return -1

    def orangesRotting(self, grid):
        orange_map={(i,j): grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))}
        q=[]
        tail=0
        visits={(i,j): False for i in range(len(grid)) for j in range(len(grid[0]))}
        for key,value in orange_map.items():
            if value!=0:
                self.o_num += 1
            if value==2:
                q.append([key,0])
                self.o_num-=1
        if self.o_num==0:
            return 0
        while tail<len(q):
            cur=q[tail]
            tail+=1
            visits[cur[0]]=True
            #print(self.o_num)
            #print(cur)
            if self.o_num==0:
                return cur[1]
            ans = self.rotten(cur.copy(),orange_map,visits,q)
            #print(self.o_num)
            if ans!=-1:
                return ans
        return -1
s=Solution()
grid=[[2,1,1],[1,1,1],[0,1,2]]
print(s.orangesRotting(grid))