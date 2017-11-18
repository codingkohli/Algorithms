def word_count_engine(document):
  if not document :
    return 0
  wordArr = document.split()
  hashDict = {}
  for word in wordArr :
    temp = cleanWord(word)
    try :
      hashDict[temp] += 1
    except :
      hashDict[temp] = 1  
  #logic to append and sort the dictionary
  hashDict_view = [ (v,k) for k,v in hashDict.iteritems() ]
  hashDict_view.sort(reverse=True)
  outRes = []
  for v,k in hashDict_view :
    strTemp = []
    strTemp.append(str(k))
    strTemp.append(str(v))
    outRes.append(strTemp)
  return outRes
    
def cleanWord(word) :
  outRes = ""
  for elem in word :
    if (ord(elem) in range(97,123)) or (ord(elem) in range(65,91)) :
      outRes = outRes + elem.lower()
  return outRes
document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
word_count_engine(document)