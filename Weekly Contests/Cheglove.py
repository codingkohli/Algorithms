"""
Code chef problem from march snackdown
Problem name : Chef and Glove
"""

from sys import stdin,stdout

def main() :
    t = int(input())
    # iterating over the test cases
    for i in range(t):
        n = int(input())
        lFin = [int(x) for x in input().split()]
        lGlove = [int(x) for x in input().split()]
        sFlag = True
        oFlag = True
        revGlove = lGlove[::-1]
        for i in range(n) :
            if sFlag or oFlag :
                if lFin[i] > lGlove[i] :
                    sFlag = False
                if lFin[i] > revGlove[i] :
                    oFlag = False
            else :
                break
        if oFlag and sFlag :
            print("both")
        elif sFlag :
            print("front")
        elif oFlag :
            print("back")
        else :
            print("none")



# calling the main method
if __name__ == "__main__" :
    main()



