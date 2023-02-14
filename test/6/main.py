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

def _tempPosition(root:tk.CTk,canvas:tk.CTkCanvas,eventInfo):
    global px,py
    px,py = eventInfo.x,eventInfo.y

def _drawLinearLine(root:tk.CTk,canvas:tk.CTkCanvas,eventInfo):
    x = eventInfo.x
    y = eventInfo.y
    size = 20
    canvas.create_line(px,py,x,y,fill="red")
    # canvas.create_rectangle(x,y,x+size,y+size,fill="red")
    pass

root = tk.CTk()
root.geometry(res)
root.title(window_name)


canvas = tk.CTkCanvas(root,width=root.winfo_width(),height=root.winfo_height(),bg="gray")
canvas.pack(padx=10,pady=10)
root.bind("<Configure>",lambda tets:_resizeEnevtHandler(root,canvas))
root.bind("<1>",lambda eventInfo:_tempPosition(root,canvas,eventInfo))
root.bind("<B1-Motion>",lambda eventInfo:_drawLinearLine(root,canvas,eventInfo))

root.mainloop()