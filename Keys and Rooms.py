# 原始 buggy Queue 类
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

# 原始 buggy Solution 类
class Solution:
    def canVisitAllRooms(self, rooms):
        q = Queue()
        line = [False] * len(rooms)
        for room in rooms[0]:
            if line[room] is False:
                q.push(room)
            line[room] = True
        line[0] = True
        while q.isEmpty() is False:
            room_tail = q.pop()
            for room in rooms[room_tail]:
                if line[room] is False:
                    q.push(room)
                line[room] = True
        return (False in line)!=True

# 测试用例
test_rooms = [
    [[1], [2], [3], []],                      # 1. 简单递进
    [[1, 3], [3, 0, 1], [2], [0]],            # 2. 有环
    [[1], []],                                # 3. 两个房间
    [[], [0]],                                # 4. room 1 有 key 但进不去
    [[1], [2], [], [1]],                      # 5. room 3 永远进不去
    [[1, 2], [2], [3], [0]],                  # 6. 所有房间访问成功（环）
    [[1], [2], [3], [4], []],                 # 7. 线性结构
    [[1, 2, 3], [], [], []],                  # 8. 初始房间全钥匙
    [[1], [2], [], [1, 0]],                   # 9. 不可达房间
]

# 执行并打印结果
for idx, rooms in enumerate(test_rooms, 1):
    try:
        sol = Solution()
        result = sol.canVisitAllRooms(rooms)
        print(f"✅ Test case {idx}: rooms = {rooms} => Result: {result}")
    except Exception as e:
        print(f"❌ Test case {idx}: rooms = {rooms} => Error: {type(e).__name__}: {e}")
