class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber:
            columnNumber -= 1
            d = columnNumber % 26
            ascii = ord('A') + d
            res = chr(ascii) + res
            columnNumber = columnNumber // 26

        return res