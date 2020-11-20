from os import listdir

filePath = "D:\FINAL-VER\VNT-VN-426-847\\" #set path folder chua TCH o day
dirPath = listdir(filePath)

smallestTchNoMinusOne = 425 #so thu chao hang nho nhat tru di 1
largestTchNo = 847 #so thu chao hang lon nhat


correctTchList = []
for i in range(largestTchNo - smallestTchNoMinusOne):
    smallestTchNoMinusOne += 1
    correctTchList.append(str(smallestTchNoMinusOne)+"_20.pdf") # _20 thay doi theo so nam/file


check = tuple(set(correctTchList) - set(dirPath))
sortCheck = sorted(check)
print(sortCheck)
