import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
res = "500x500"
window_name = "Paint"

def _resizeEnevtHandler(root:tk.CTk,canvas:tk.CTkCanvas):
    canvas.configure(width=root.winfo_width(),height=root.winfo_height())

isInitLine = True
fillcolor = "White"

DrawObjList = []

def _LineDraw(root:tk.CTk,canvas:tk.CTkCanvas,eventInfo,buttonState):
    global px,py,Line,ppx,ppy,DrawObjList
    if(buttonState == "P"):
        px,py = eventInfo.x,eventInfo.y
    elif(buttonState == "R"):
        x,y = eventInfo.x,eventInfo.y
        id = canvas.create_line(px,py,x,y,fill=fillcolor,width=10)
        DrawObjList.append(id)
    elif(buttonState == "M"):
        global isInitLine
        if(isInitLine == True):
            isInitLine = False
        else:
            canvas.delete(Line)
        x,y = eventInfo.x,eventInfo.y
        ppx,ppy = x,y
        tag = str(x)+":"+str(y)
        Line = tag
        canvas.create_line(px,py,x,y,fill=fillcolor,width=10,tags=tag)

isInitRect = True

def _CreateRectangle(root:tk.CTk,canvas:tk.CTkCanvas,eventInfo,buttonState):
    global px,py,Rect,ppx,ppy,DrawObjList
    if(buttonState == "P"):
        px,py = eventInfo.x,eventInfo.y
    elif(buttonState == "R"):
        x,y = eventInfo.x,eventInfo.y
        id = canvas.create_rectangle(px,py,x,y,fill=fillcolor,outline="",width=0)
        DrawObjList.append(id)
    elif(buttonState == "M"):
        global isInitRect
        if(isInitRect == True):
            isInitRect = False
        else:
            canvas.delete(Rect)
        x,y = eventInfo.x,eventInfo.y
        ppx,ppy = x,y
        tag = str(x)+":"+str(y)
        Rect = tag
        canvas.create_rectangle(px,py,x,y,fill=fillcolor,tags=tag,outline="",width=0)

isInitTri = True
StepTir = "FirstOp"
isInitLineTir = True
TirPosiList = []

def _CreateTriangle(root:tk.CTk,canvas:tk.CTkCanvas,eventInfo,buttonState):
    global px,py,Tri,Line,ppx,ppy,StepTir,TirPosiList,DrawObjList
    if(StepTir == "FirstOp"):
        if(buttonState == "P"):
            px,py = eventInfo.x,eventInfo.y
        elif(buttonState == "R"):
            x,y = eventInfo.x,eventInfo.y
            id = canvas.create_line(px,py,x,y,fill=fillcolor,width=0)
            DrawObjList.append(id)
            TirPosiList.append(px)
            TirPosiList.append(py)
            TirPosiList.append(x)
            TirPosiList.append(y)
            StepTir = "SecOp"
        elif(buttonState != "Mo"):
            global isInitLineTir
            if(isInitLineTir == True):
                isInitLineTir = False
            else:
                canvas.delete(Line)
            x,y = eventInfo.x,eventInfo.y
            ppx,ppy = x,y
            tag = str(x)+":"+str(y)
            Line = tag
            canvas.create_line(px,py,x,y,fill=fillcolor,width=10,tags=tag)

    elif(StepTir == "SecOp"):
        if((buttonState == "P") or (buttonState == "Mo")):
            global isInitTri
            if(isInitTri == True):
                isInitTri = False
            else:
                canvas.delete(Tri)
            x,y = eventInfo.x,eventInfo.y
            ppx,ppy = x,y
            tag = str(x)+":"+str(y)
            Tri = tag
            canvas.create_polygon(TirPosiList[0],TirPosiList[1],TirPosiList[2],TirPosiList[3],x,y,fill=fillcolor,tags=tag,outline="",width=0)
        elif(buttonState == "R"):
            x,y = eventInfo.x,eventInfo.y
            id = canvas.create_polygon(TirPosiList[0],TirPosiList[1],TirPosiList[2],TirPosiList[3],x,y,fill=fillcolor,outline="",width=0)
            DrawObjList.append(id)
            TirPosiList.clear()
            StepTir = "FirstOp"
        else:
            # global isInitTri
            if(isInitTri == True):
                isInitTri = False
            else:
                canvas.delete(Tri)
            x,y = eventInfo.x,eventInfo.y
            ppx,ppy = x,y
            tag = str(x)+":"+str(y)
            Tri = tag
            canvas.create_polygon(TirPosiList[0],TirPosiList[1],TirPosiList[2],TirPosiList[3],x,y,fill=fillcolor,tags=tag,outline="",width=0)

        





iscontrolpanelExist = False

def _changeColor(color:str):
    if(color != "New color"):
        global fillcolor
        fillcolor = color

CretateMode = "Line"

def _CreateThing(root:tk.CTk,canvas:tk.CTkCanvas,eventInfo,ButtonState):
    global CretateMode
    modeList = ["Line","Rectangle","Triangle","delete"]
    # funcList = [_LineDraw(root,canvas,eventInfo,ButtonState),_CreateRectangle(root,canvas,eventInfo,ButtonState)]
    if(CretateMode == modeList[0]):
        _LineDraw(root,canvas,eventInfo,ButtonState)
    if(CretateMode == modeList[1]):
        _CreateRectangle(root,canvas,eventInfo,ButtonState)
    if(CretateMode == modeList[2]):
        _CreateTriangle(root,canvas,eventInfo,ButtonState)


def _chnageMode(mode:str):
    global CretateMode
    CretateMode = mode

def _cavasClear(canvas:tk.CTkCanvas):
    global DrawObjList
    for item in DrawObjList:
        canvas.delete(item)
    DrawObjList.clear()
    canvas.update()

def _controlPanel(root:tk.CTk,canvas:tk.CTkCanvas):
    global iscontrolpanelExist
    if(iscontrolpanelExist == False):
        iscontrolpanelExist = True
        optionWindow = tk.CTkToplevel(root)
        optionWindow.title("Option Panel")
        optionWindow.geometry("300x200")
        modeButton = tk.CTkSegmentedButton(optionWindow,values=["Line","Rectangle","Triangle","delete"])
        modeButton.set("Line")
        modeButton.pack(padx=10,pady=10)
        colorButton = tk.CTkSegmentedButton(optionWindow,values=["White","Black","Red","Green","New color"])
        colorButton.set("White")
        colorButton.pack(padx=10,pady=10)
        canvasClearButton = tk.CTkButton(optionWindow,text="Clear canvas")
        canvasClearButton.bind("<1>",lambda event:_cavasClear(canvas))
        canvasClearButton.pack(padx=10,pady=10)
        optionWindow.bind("<1>",lambda event:[_changeColor(colorButton.get()),_chnageMode(modeButton.get())])
        optionWindow.mainloop()



if __name__ == "__main__":
    root = tk.CTk()
    root.geometry(res)
    root.title(window_name)

    canvas = tk.CTkCanvas(root,width=root.winfo_width(),height=root.winfo_height(),bg="gray")
    canvas.pack(padx=10,pady=10)
    root.bind("<Configure>",lambda tets:_resizeEnevtHandler(root,canvas))
    root.bind("<Motion>",lambda event:_controlPanel(root,canvas))
    canvas.bind("<1>",lambda enevtInfo:[_CreateThing(root,canvas,enevtInfo,"P")])
    canvas.bind("<ButtonRelease-1>",lambda enevtInfo:_CreateThing(root,canvas,enevtInfo,"R"))
    canvas.bind("<B1-Motion>",lambda enevtInfo:_CreateThing(root,canvas,enevtInfo,"M"))
    canvas.bind("<Motion>",lambda eventInfo:_CreateThing(root,canvas,eventInfo,"Mo"))

    # optionButton = tk.CTkButton(root,text="Open option panel")
    # optionButton.bind("<1>",lambda event:_controlPanel(root))
    # optionButton.pack(padx=10,pady=10)

    root.mainloop()