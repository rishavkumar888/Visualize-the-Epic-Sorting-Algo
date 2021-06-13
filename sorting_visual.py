import time




def getColorArray(dataLen,head,tail,border,currIdx,isSwapping=False):
    colorArray=[]
    for i in range(dataLen):
        
        if i>=head and i<=tail:
            colorArray.append('grey')
        else:
            colorArray.append('white')
        
        if i == tail:
            colorArray[i]='blue'
        elif i=='border':
            colorArray[i]='red'
        elif i == currIdx:
            colorArray[i]='yellow'
            
        if isSwapping:
            if i ==border or i == currIdx:
                colorArray[i]='green'
                
    return colorArray