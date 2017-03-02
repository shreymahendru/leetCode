import collections
class MyStack(object):
    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        print "atttt starte "
        print q
        for _ in range(len(q) - 1):
            b = q.popleft()
            print b
            q.append(b)
            print q
        # print q
    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(36)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
