import time

def shell_sort(data,drawData,timeSpeed):
    n=len(data)
    
    color=[]
    for i in range(len(data)):
        color.append('red')
    drawData(data,color)
    
    gap=n//2
    
    while(gap>0):
        for i in range(gap,n):
            temp=data[i]
            
            color[i]='blue'
            drawData(data,color)
            time.sleep(timeSpeed)
            
            j=i
            while(j>=gap and data[j-gap]>temp):
                if(i!=j):
                    color[j]='black'
                time.sleep(timeSpeed)
                drawData(data,color)
                data[j]=data[j-gap]
                j-=gap
            data[j]=temp
            for l in range(len(data)):
                color[l]='red'
        gap//=2