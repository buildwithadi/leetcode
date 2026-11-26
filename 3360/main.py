class Solution:
    def canAliceWin(self, n: int) -> bool:
        stone = n
        removeStone = 10
        aliceTurn = True

        while stone - removeStone >= 0:
            if aliceTurn:
                aliceTurn = False
            elif not aliceTurn:
                aliceTurn = True
            
            stone = stone - removeStone
            removeStone = removeStone - 1

        return not aliceTurn