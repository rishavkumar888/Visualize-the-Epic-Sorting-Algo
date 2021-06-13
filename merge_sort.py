import time


def merge(data,left,mid,right,drawData,tickTime):
    
    color=[]
    
    for i in range(len(data)):
        if(i>=left and i<=mid):
            color.append('blue')
        elif(i>mid and i<=right):
            color.append('black')
        else:
            color.append('grey')
            
    drawData(data,color)
    
    n1=int(mid-left+1)
    n2=int(right-mid)
    
    l=[]
    r=[]
    
    for i in range(0,n1):
        l.append(data[int(left+i)])
        
    for i in range(0,n2):
        r.append(data[int(mid+1+i)])
        
    i=int(0)
    j=int(0)
    k=int(left)
    
    while(i<n1 and j<n2):
        if(l[i]<=r[j]):
            data[k]=l[i]
            color[int(left+i)],color[int(k)]=color[int(k)],color[int(left+i)]
            k+=1
            i+=1
        else:
            data[k]=r[j]
            color[int(mid+1+j)],color[int(k)]=color[int(k)],color[int(mid+1+j)]
            k+=1
            j+=1
        drawData(data,color)
        time.sleep(tickTime)
            
    while(i<n1):
        data[k]=l[i]
        k+=1
        i+=1
        #time.sleep(tickTime)
    
    while(j<n2):
        data[k]=r[j]
        k+=1
        j+=1
        #time.sleep(tickTime)
        

def merge_sort(data,head,tail,drawData,tickTime):
    if(head<tail):
        mid=int((head+tail)/2)
        merge_sort(data,head,mid,drawData,tickTime)
        merge_sort(data,mid+1,tail,drawData,tickTime)
        merge(data,head,mid,tail,drawData,tickTime)
        