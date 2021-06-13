from tkinter import *
from tkinter import ttk
import random
from bubble_sort import bubble_sort
from quick_sort import quick_sort
from merge_sort import merge_sort
from bucket_sort import bucket_sort
from comb_sort import comb_sort
from shell_sort import shell_sort

root=Tk()
root.title("sorting algorithm")
root.maxsize(900,600)
root.config(bg='black')


selected_alg=StringVar()
data=[]

def drawData(data,colorArray):
    canvas.delete("all")
    c_height=380
    c_width=580
    x_width=(c_width)/(len(data))
    offset=10
    spacing=0
    
    normalizeData=[i/max(data) for i in data]
    
    for i, height in enumerate(normalizeData):
        
        #top left
        x0=i*x_width+offset+spacing
        y0=c_height-height*340
        #bottom right
        x1=(i+1)*x_width+offset
        y1=c_height
        
        print("i= "+str(i)+"  height= "+str(height)+"   "+str(x0)+","+str(y0)+" : "+str(x1)+","+str(y1))
        
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
        
    root.update_idletasks()

def Generate():
    
    global data
    
    minVal=int(minEntry.get())
    maxVal=int(maxEntry.get())
    size=int(sizeEntry.get())
        
    
    data=[]
    for _ in range(size):
        data.append(random.randrange(minVal,maxVal+1))
        
    
    drawData(data,['red' for x in range(len(data))])
    
def StartAlgorithm():
    
    global data
    
    if not data: return
    
    if(algMenu.get()=='Quick Sort'):
        quick_sort(data,0,len(data)-1,drawData,speedScale.get())
        drawData(data,['green' for x in range(len(data))])
    elif algMenu.get()=='Bubble Sort':
        bubble_sort(data,drawData,speedScale.get())
    elif algMenu.get()=='Merge Sort':
        merge_sort(data,0,len(data)-1,drawData,speedScale.get())
        drawData(data,['green' for x in range(len(data))])
    elif algMenu.get()=='Bucket Sort':
        bucket_sort(data,5,['red','blue','black','yellow','pink'],drawData,speedScale.get())
    elif algMenu.get()=='Comb Sort':
        comb_sort(data,drawData,speedScale.get())
        drawData(data,['green' for x in range(len(data))])
    elif algMenu.get()=='Shell Sort':
        shell_sort(data,drawData,speedScale.get())
        drawData(data,['green' for x in range(len(data))])

UI_frame=Frame(root,width=600,height=200,bg='grey')
UI_frame.grid(row=0,column=0,padx=10,pady=5)


canvas=Canvas(root,width=600,height=380,bg='white')
canvas.grid(row=1,column=0,padx=10,pady=5)

#row[0]
Label(UI_frame,text="Algorithm: ",bg='grey').grid(row=0,column=0,padx=5,pady=5,sticky=W)
algMenu=ttk.Combobox(UI_frame,textvariable=selected_alg,values=['Bubble Sort','Quick Sort','Merge Sort','Bucket Sort','Comb Sort','Shell Sort'])
algMenu.grid(row=0,column=1,padx=5,pady=5)
algMenu.current(0)

speedScale=Scale(UI_frame,from_=0.01,to=1.0,length=200,digits=2,resolution=0.01,orient=HORIZONTAL,label="Select Speed")
speedScale.grid(row=0,column=2,padx=5,pady=5)
Button(UI_frame,text="Start",command=StartAlgorithm,bg='red').grid(row=0,column=3,padx=5,pady=5)

#row[1]
sizeEntry=Scale(UI_frame,from_=3,to=100,length=200,resolution=1,orient=HORIZONTAL,label="Data Size")
sizeEntry.grid(row=1,column=0,padx=5,pady=5)

minEntry=Scale(UI_frame,from_=0,to=10,length=200,resolution=1,orient=HORIZONTAL,label="Min Entry")
minEntry.grid(row=1,column=1,padx=5,pady=5)

maxEntry=Scale(UI_frame,from_=10,to=100,length=200,resolution=1,orient=HORIZONTAL,label="Max Entry")
maxEntry.grid(row=1,column=2,padx=5,pady=5)

Button(UI_frame,text="Generate",command=Generate,bg='white').grid(row=1,column=3,padx=5,pady=5)

root.mainloop()