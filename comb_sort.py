import time

def get_next_gap(gap):
    gap=(gap*10)/13
    if(gap<1):
        return 1
    return gap

def comb_sort(data,drawData,tickSpeed):
    n=len(data)
    gap=n
    swapped=True
    
    color=[]
    for i in range(n):
        color.append('black')
        
    drawData(data,color)
    
    time.sleep(tickSpeed)
    
    while(gap!=1 or swapped==1):
        
        gap=get_next_gap(gap)
        for j in range(int(n-gap+1),n):
            color[j]='blue'
        drawData(data,color)
        time.sleep(tickSpeed)
        swapped=False
        for i in range(0,int(n-gap)):
            if(data[i]>data[int(i+gap)]):
                data[i],data[int(i+gap)]=data[int(i+gap)],data[i]
                color[i],color[int(i+gap)]=color[int(i+gap)],color[i]
                drawData(data,color)
                time.sleep(tickSpeed)
                swapped=True