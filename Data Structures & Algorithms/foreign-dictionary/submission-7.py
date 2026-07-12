class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: [] for w in words for c in w}
        indegree = {c: 0 for c in adjList}


        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            if w1[: minLen] == w2[: minLen] and len(w1) > len(w2):
                return ""
            
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w2[j]].append(w1[j])
                    indegree[w1[j]] += 1
                    break

        
        q = deque()
        res = []
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        while q:
            c = q.popleft()
            for nei in adjList[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

            res.append(c)

        if len(res) != len(indegree):
            return ""

        return ''.join(res[::-1])
