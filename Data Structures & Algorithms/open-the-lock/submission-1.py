class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)

        visited = set()

        q = deque([(target, 0)])

        while q:
            comb, turns = q.popleft()
            if comb in visited or comb in deadends:
                continue
            if comb == "0000":
                return turns
            visited.add(comb)
            for i in range(4):
                newComb1 = comb[:i] + str((int(comb[i]) - 1 + 10) % 10) + comb[i + 1:]
                newComb2 = comb[:i] + str((int(comb[i]) + 1) % 10) + comb[i + 1:]
                q.append((newComb1, turns + 1))
                q.append((newComb2, turns + 1))

        return -1


        

            
            
            