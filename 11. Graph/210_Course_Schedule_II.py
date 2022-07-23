class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #dict {course: prerequisites}
        pre = collections.defaultdict(list)
        for crs, p in prerequisites:
            pre[crs].append(p)
        res = []
        visit, resSet = set(), set()
        def dfs(c):
            # add all the prereq before c recusively
            # c is the prereq of c -> not able to finish all courses
            if c in visit:
                return False
            #when the prerequisite has been satified
            if c in resSet:
                return True
            
            visit.add(c)
            for p in pre[c]:
                if not dfs(p):
                    return False
            visit.remove(c)
            # append all the prerequites of c before appending c
            res.append(c)
            resSet.add(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return res
