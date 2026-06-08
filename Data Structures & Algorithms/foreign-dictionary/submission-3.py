class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for w in words for c in w}
        inDegree = {c: 0 for c in adjList}

        for i in range(len(words) - 1):
            firstWord = words[i]
            secondWord = words[i + 1]

            minLength = min(len(firstWord), len(secondWord))

            if len(firstWord) > len(secondWord) and firstWord[: minLength] == secondWord[: minLength]:
                return ""
            
            for j in range(minLength):
                if firstWord[j] != secondWord[j]:
                    if firstWord[j] not in adjList[secondWord[j]]:
                        adjList[secondWord[j]].add(firstWord[j])
                        inDegree[firstWord[j]] += 1
                    break

        queue = deque()
        res = []
        for c in inDegree:
            if inDegree[c] == 0:
                queue.append(c)
        print(queue)
        while queue:
            char = queue.popleft()
            res.append(char)
            for pre in adjList[char]:
                inDegree[pre] -= 1
                if inDegree[pre] == 0:
                    queue.append(pre)

        if len(res) != len(inDegree):
            return ""
        
        return "".join(res[::-1])

                

            

            