class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def getHash(string):
            hash = []
            for i in range(len(string) - 1):
                first = string[i]
                second = string[i + 1]
                hash.append(chr((ord(second) - ord(first)) % 26 + ord('a')))
            
            return ''.join(hash)

        groups = defaultdict(list)

        for string in strings:
            hash = getHash(string)
            groups[hash].append(string)

        return list(groups.values())