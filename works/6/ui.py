import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass
import customtkinter as tk
from selenium.webdriver.common.by import By
from Item import baseDataStructure

WIDTH = 400

class setTarget:
    def __init__(self,root:tk.CTk) -> None:
        self.root = root
        self.ID = ""
        self.IDValue = ""
        self.optionList = [By.ID,
                            By.XPATH,
                            By.LINK_TEXT,
                            By.PARTIAL_LINK_TEXT,
                            By.NAME,
                            By.TAG_NAME,
                            By.CLASS_NAME,
                            By.CSS_SELECTOR]
        # self.showForm()

    def showForm(self,tab):
        content = []
        self.frame = tk.CTkFrame(tab)
        self.label = tk.CTkLabel(self.frame,text="Choose mode and enter value.")
        self.label.grid(row=0,column=0)
        self.select = tk.CTkOptionMenu(self.frame,values=self.optionList)
        self.select.grid(row=1,column=0)
        self.Entry = tk.CTkEntry(self.frame,width=WIDTH)
        self.Entry.grid(row=2,column=0)
        # This button should be bind to worker when this class is used.
        self.button = tk.CTkButton(self.frame,text="Register")
        self.button.grid(row=3,column=0)
        self.frame.pack()
        content.append(self.label)
        content.append(self.Entry)
        content.append(self.button)
        content.append(self.select)
        for widget in content:
            widget:tk.CTkLabel
            widget.grid_configure(padx=10,pady=10)

    # TODO: setContent function has been changed with new idea so args need to be changed.
    def getData(self,data:baseDataStructure):
        data.setContent(self.select.get(),self.Entry.get())


class setScript:
    def __init__(self,root:tk.CTk) -> None:
        self.root = root
        self.script = ""
        # self.showForm()

    def showForm(self,tab):
        content = []
        self.frame = tk.CTkFrame(tab)
        self.label = tk.CTkLabel(self.frame,text="Please enter your js.")
        self.label.grid(row=0,column=0)
        self.textBox = tk.CTkTextbox(self.frame,width=WIDTH)
        self.textBox.grid(row=1,column=0)
        # This button should be bind to worker when this class is used.
        self.button = tk.CTkButton(self.frame,text="Register")
        self.button.grid(row=2,column=0)
        self.frame.pack()
        content.append(self.label)
        content.append(self.button)
        content.append(self.textBox)
        for widget in content:
            widget:tk.CTkLabel
            widget.grid_configure(padx=10,pady=10)

    # TODO: setContent function has been changed with new idea so args need to be changed.
    def getData(self,data:baseDataStructure):
        # data.setScript(self.textBox.get(1.0,tk.END))
        pass


class setWait:
    def __init__(self,root:tk.CTk) -> None:
        self.content = []
        self.root = root
        # self.showForm()

    def showForm(self,tab):
        content = []
        self.frame = tk.CTkFrame(tab)
        self.label = tk.CTkLabel(self.frame,text="How long interval is? Please Enter (sec)")
        self.label.grid(row=0,column=0)
        self.Entry = tk.CTkEntry(self.frame,width=WIDTH)
        self.Entry.grid(row=1,column=0)
        # This button should be bind to worker when this class is used.
        self.button = tk.CTkButton(self.frame,text="Register")
        self.button.grid(row=2,column=0)
        self.frame.pack()
        content.append(self.label)
        content.append(self.button)
        content.append(self.Entry)
        for widget in content:
            widget:tk.CTkLabel
            widget.grid_configure(padx=10,pady=10)

    # TODO: setContent function has been changed with new idea so args need to be changed.
    def getData(self,data:baseDataStructure):
        data.setTime(self.Entry.get())

class orderDefineUI:
    def __init__(self) -> None:
        
        pass


class mainUI:
    def __init__(self,root:tk.CTk) -> None:
        self.root = root
        self.elemSelecUI = setTarget(root)
        self.ScriptUI = setScript(root)
        self.TimeUI = setWait(root)
        self.RegisterUI()

    def RegisterUI(self):
        self.tabs = tk.CTkTabview(self.root)
        self.tabs.add("Element")
        self.tabs.add("Script")
        self.tabs.add("sleep")
        self.elemSelecUI.showForm(self.tabs.tab("Element"))
        self.ScriptUI.showForm(self.tabs.tab("Script"))
        self.TimeUI.showForm(self.tabs.tab("sleep"))
        self.tabs.pack()

    def UnSortedThingsList(self):
        pass

    def SortedThingsList(self):
        pass

if __name__ == "__main__":
    import ctypes
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass
    import customtkinter as tk
    window_name = "UI test window"
    root = tk.CTk()
    root.title(window_name)
    ins = mainUI(root)


    root.mainloop()