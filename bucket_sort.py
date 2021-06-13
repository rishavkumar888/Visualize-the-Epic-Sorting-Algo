import time

def bucket_sort(data,noOfBucket,colortemp,drawData,tickSpeed):
    minEle=min(data)
    maxEle=max(data)
    
    color=[]
    for i in range(len(data)):
        color.append('orange')
    
    drawData(data,color)
    time.sleep(tickSpeed)
    
    ran=(maxEle-minEle)/noOfBucket
    
    lis=[]
    
    for i in range(noOfBucket):
        lis.append([])
        
    for i in range(len(data)):
        dif=(data[i]-minEle)/ran-int((data[i]-minEle)/ran)
        
        if(dif==0 and data[i]!=minEle):
            lis[int((data[i]-minEle)/ran)-1].append(data[i])
            color[i]=colortemp[int((data[i]-minEle)/ran)-1]
            
        else:
            lis[int((data[i]-minEle)/ran)].append(data[i])
            color[i]=colortemp[int((data[i]-minEle)/ran)]
        
        time.sleep(tickSpeed)
        drawData(data,color)
            
    for i in range(len(lis)):
        if(len(lis[i])!=0):
            lis[i].sort()
    
    k=0
    for i in lis:
        if i:
            for j in i:
                data[k]=j
                time.sleep(tickSpeed)
                color[k]='green'
                drawData(data,color)
                k+=1