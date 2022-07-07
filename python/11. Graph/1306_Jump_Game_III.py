# BFS to search for a possible path
# time: O(n)
# space: O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l = len(arr)
        q = deque()
        q.append(start)
        
        while q:
            
            for i in range(len(q)):
                point = q.popleft()
                if arr[point] == 0: return True
                
                # the left point
                if point - arr[point] in range(l):
                    if arr[point - arr[point]] == 0: return True
                    elif arr[point - arr[point]] > 0: q.append(point - arr[point])
                # the right point
                if point + arr[point] in range(l):
                    if arr[point + arr[point]] == 0: return True
                    elif arr[point + arr[point]] > 0: q.append(point + arr[point])
                #mark point as visited
                arr[point] = -1
        # if no path found
        return False
