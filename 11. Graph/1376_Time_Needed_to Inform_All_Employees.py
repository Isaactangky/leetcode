class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # head -> manager -> subordinate
        # time needed is the maximum of the inform time for the paths
        # dfs on all the pathes
        # when informTime[e] == 0: the path ends, update ans if time of the path > ans
        sub_dict = collections.defaultdict(list)
        ans = [0]
        for i in range(n):
            sub_dict[manager[i]].append(i)
        #head index
        head = sub_dict[-1][0]
        
        
        def dfs(e, time):
            if informTime[e] == 0:
                ans[0] = max(time, ans[0])
                return
            
            mTime = informTime[e] 
            for s in sub_dict[e]:
                dfs(s, time + mTime)
        dfs(head, 0)
        return ans[0]
