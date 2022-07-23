# similar to num of islands questions
# bfs all the connected cities when finding a city not in visit
# time: O(m * m) m: num of cities ( length of isConnected or lengthe of isConnected[0])
# space: O(m) for the visit set
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visit = set()
        l = len(isConnected)
        num = 0
        for i in range(l):
            if i in visit: continue
            
            visit.add(i)
            q = deque()
            q.append(i)
            # bfs all the connected provinces
            while q:
                for k in range(len(q)):
                    index = q.popleft()
                    for j in range(l):
                        if index != j and isConnected[index][j] == 1 and j not in visit:
                            visit.add(j)
                            q.append(j)
            #increment num after visiting all cities in the same province
            num += 1
        
        return num
        
