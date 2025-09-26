class Queue:
    def __init__(self):
        self.queue = []
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def push(self, val):
        self.queue.append(val)
        self.head = self.queue[self.length]
        self.length += 1

    def pop(self):
        self.length -= 1
        return self.queue.pop(0)

    def peak(self):
        self.tail = self.queue[0]
        return self.tail
class Solution:
    def findCircleNum(self, isConnected):
        num=len(isConnected)
        graph=[[] for _ in range(num)]
        print(graph)
        for i in range(num):
            for j in range(num):
                if isConnected[i][j]==1:
                    graph[i].append(j)
        print(graph)
        vers=[False]*num
        pro=0
        for i in range(num):
            if vers[i]==False:
                vers[i]=True
                pro+=1
                q=Queue()
                for ver in graph[i]:
                    if vers[ver]==False:
                        q.push(ver)
                while q.isEmpty() is False:
                    ver=q.pop()
                    vers[ver]=True
                    for p in graph[ver]:
                        if vers[p]==False:
                            q.push(p)
        return pro