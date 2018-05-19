import os

def delmSniffer (fp) :
    if not fp :
        return
    line1 = fp.readline()
    line2 = fp.readline()
    delList = [",", "|", "!", ";"]
    fileDelm = ""
    colList = []
    for delm in delList:
        headRecord = line1.split(delm)
        record2 = line2.split(delm)
        if len(headRecord) > 1 and len(record2) == len(headRecord):
            fileDelm = delm
            for val in headRecord:
                if val and val != '\n':
                    colList.append(val)
            print("Delinator is : " + delm)
            print("Col List is as follows :")
            print(colList)
            return colList



def recursiveRead (dataDir) :
    listOfFiles = os.listdir(dataDir)
    colList = []
    for dataFiles in listOfFiles:
        fileLoc = dataDir + '/' + dataFiles
        fp = open(fileLoc,'r')
        colList = colList + delmSniffer(fp)
        fp.close()
    return colList


def getUniqueColumns(colList) :
    if not colList :
        return
    uniqueCols = set(colList)
    return uniqueCols

dataDir = './DataAnalysis'
colList = recursiveRead(dataDir)
print("Columns of all the files is :")
print(colList)

uniqueCols = getUniqueColumns(colList)
print("Unique Columns in a list")
print(uniqueCols)

