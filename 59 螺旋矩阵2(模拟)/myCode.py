class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        target = n * n
        num = 1
        levelBegin = 0
        levelEnd = n-1
        verticalBegin = 0
        verticalEnd = n-1
        result = [[0 for i in range(n)] for j in range(n)]
        while num <= target and verticalBegin < verticalEnd:
            # print(verticalBegin, verticalEnd, levelBegin, levelEnd)
            i = verticalBegin
            j = levelBegin
            while j < levelEnd:
                result[i][j] = num
                j += 1
                num += 1
            levelEnd -= 1
            while i < verticalEnd:
                result[i][j] = num
                i += 1
                num += 1
            verticalEnd -= 1
            while j > levelBegin:
                result[i][j] = num
                j -= 1
                num += 1
            levelBegin += 1
            while i > verticalBegin:
                result[i][j] = num
                i -= 1
                num += 1
            verticalBegin += 1
        if verticalBegin == verticalEnd:
            result[verticalBegin][levelBegin] = target
        return result
