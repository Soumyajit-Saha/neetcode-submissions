class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: [] for word in words for c in word}
        indegree = {c: 0 for word in words for c in word}


        for i in range(1, len(words)):
            first = words[i - 1]
            second = words[i]

            minLen = min(len(first), len(second))

            if first[: minLen] == second[: minLen] and len(first) > len(second):
                return ""
            for j in range(minLen):
                if first[j] != second[j]:
                    adjList[first[j]].append(second[j])
                    indegree[second[j]] += 1
                    break

        q = deque()
        for c in indegree.keys():
            if indegree[c] == 0:
                q.append(c)

        res = []
        while q:
            c = q.popleft()
            for nei in adjList[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            res.append(c)

        if len(res) != len(indegree.keys()):
            return ""

        return ''.join(res)
