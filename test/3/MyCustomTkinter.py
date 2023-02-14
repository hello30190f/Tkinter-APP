import customtkinter
from typing import Union, Tuple, List, Optional
# import customtkinter as tk

class MyCustomTkinter(customtkinter.CTkFrame,customtkinter.CTkLabel):

    def __init__():
        super.__init__()

    class LabelFrame(customtkinter.CTkFrame,customtkinter.CTkLabel):
        def __init__(self,
                     master: any,
                     width: int = 200,
                     height: int = 200,
                     text: str = "Wow this is working",
                     corner_radius: Optional[Union[int, str]] = None,
                     border_width: Optional[Union[int, str]] = 0.0,

                     bg_color: Union[str, Tuple[str, str]] = "transparent",
                     fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                     border_color: Optional[Union[str, Tuple[str, str]]] = None,

                     background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None,
                     overwrite_preferred_drawing_method: Union[str, None] = None,
                     **kwargs):
            self._background_corner_colors = background_corner_colors
            self._border_width = border_width
            self._corner_radius = corner_radius
            self._fg_color = fg_color
            self._border_color = border_color
            self._overwrite_preferred_drawing_method = overwrite_preferred_drawing_method
            super().__init__(master=master, bg_color=bg_color, width=width, height=height, **kwargs)
            self.MainFrame = customtkinter.CTkFrame(master,width=width+20,height=height+30)
            self.Label = customtkinter.CTkLabel(self.MainFrame,text=text)
            self.Frame = customtkinter.CTkFrame(self.MainFrame,width=width,height=height)


        def grid(self,**Kwargs):
            self.MainFrame.grid(row=Kwargs["row"],column=Kwargs["column"],padx=10,pady=10)
            self.Label.place(x=10,y=0)
            self.Frame.place(x=10,y=20)

        def pack(self,**Kwargs):
            self.MainFrame.pack(**Kwargs)
            self.Label.place(x=10,y=0)
            self.Frame.place(x=10,y=20)


if __name__ == "__main__":
    import customtkinter as tk
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass
    res = "1000x1000"
    window_name = "ex"
    root = tk.CTk()
    root.geometry(res)
    root.title(window_name)

    LabelFrameTest = MyCustomTkinter.LabelFrame(root,text="Hello world",width=200,height=300)
    LabelFrameTest.pack()

    root.mainloop()

