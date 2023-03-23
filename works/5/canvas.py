import customtkinter as tk


class boxAndPhysics:

    def _resizeEnevtHandler(self,root:tk.CTk,canvas:tk.CTkCanvas):
        canvas.configure(width=root.winfo_width(),height=root.winfo_height())

    def __init__(self,root:tk.CTk):
        self.canvas = tk.CTkCanvas(root,width=root.winfo_width(),height=root.winfo_height(),bg="gray")
        self.canvas.pack(padx=10,pady=10)
        self.canvas.bind("<1>",lambda event:self._canvasHandlerMousePressed(event))
        self.canvas.bind("<B1-Motion>",lambda event:self._canvasHandlerMouseMoving(event))
        self.canvas.bind("<ButtonRelease-1>",lambda event:self._canvasHandlerMouseReleased(event))
        root.bind("<Configure>",lambda event:self._resizeEnevtHandler(root,self.canvas))
        self.x = 10
        self.y = 10
        self.size = 10

    def _canvasHandlerMousePressed(self,event):
        # print("press")
        pass

    def _canvasHandlerMouseMoving(self,event):
        # print(event.x)
        pass

    def _canvasHandlerMouseReleased(self,event):
        # print("release")
        pass

    def _returnRectSize(self,x,y):
        return x,y,x+self.size,y+self.size

    def _drawBox(self,x,y):
        self.canvas:tk.CTkCanvas
        self.canvasId = self.canvas.create_rectangle(self.size(x,y))

