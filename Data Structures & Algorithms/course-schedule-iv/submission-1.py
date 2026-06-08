class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        preReq = {i: set() for i in range(numCourses)}

        for pre, crs in prerequisites:
            # we store the pre in key as we need to compute the pre req of pre before we go to crs
            adjList[pre].append(crs)
            indegree[crs] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            pre = q.popleft()
            for crs in adjList[pre]:
                preReq[crs].add(pre)
                preReq[crs].update(preReq[pre])
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs) 

        return [u in preReq[v] for u, v in queries]
