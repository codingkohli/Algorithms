class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        dpMat = [[1] * N for i in range(N)]
        leftMat = [[0] * N for i in range(N)]
        rightMat = [[0] * N for i in range(N)]
        upMat = [[0] * N for i in range(N)]
        downMat = [[0] * N for i in range(N)]
        for mine in mines:
            dpMat[mine[0]][mine[1]] = 0
        # print(dpMat)
        # calculating the left mat
        for i in range(N):
            temp = 0
            for j in range(N):
                leftMat[i][j] = temp
                if dpMat[i][j] == 0:
                    temp = 0
                    leftMat[i][j] = 0
                else:
                    temp += 1

        # calculating the right mat
        for i in range(N - 1, -1, -1):
            temp = 0
            for j in range(N - 1, -1, -1):
                rightMat[i][j] = temp
                if dpMat[i][j] == 0:
                    temp = 0
                    rightMat[i][j] = 0
                else:
                    temp += 1

        # calculating the downmat
        for i in range(N - 1, -1, -1):
            temp = 0
            for j in range(N - 1, -1, -1):
                downMat[j][i] = temp
                if dpMat[j][i] == 0:
                    temp = 0
                    downMat[j][i] = 0
                else:
                    temp += 1

        outRes = 0
        # calculating the upMat
        for i in range(N):
            temp = 0
            for j in range(N):
                upMat[j][i] = temp
                if dpMat[j][i] == 0:
                    temp = 0
                    upMat[j][i] = 0
                else:
                    temp += 1
                    tempOrd = 1 + min(leftMat[j][i], rightMat[j][i], upMat[j][i], downMat[j][i])
                    outRes = max(tempOrd, outRes)

        # traversing through the matrix
        """
        for i in range(N) :
            for j in range(N) :
                if dpMat[i][j] == 1 :
                    tempOrd = 1 + min(leftMat[i][j],rightMat[i][j],upMat[i][j],downMat[i][j])
                    outRes = max(tempOrd,outRes)
        """
        # returning the value
        return outRes

        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """