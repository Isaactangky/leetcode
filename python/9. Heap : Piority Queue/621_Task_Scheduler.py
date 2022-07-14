
"""
count the letters
maxHeap: process the most freq letter first, the add it to queue
queue: store the letters in cool down
time: O(m * n) m: len(tasks)
space: O(26)
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap =  [- count for count in counts.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0
        
        while maxHeap or q:
            time += 1
            # pop the most freq task
            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val < 0:
                    push_time = time + n
                    q.append((push_time, val))
            # push the val back when it has cooled down
            if q and q[0][0] == time:
                push_val = q.popleft()[1]
                heapq.heappush(maxHeap, push_val)

        return time
        