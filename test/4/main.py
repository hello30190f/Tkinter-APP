import customtkinter as tk
import socket
import http
import qemu
import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


def _prototype(root:tk.CTk):
    # prefix mean
    # I decide prefix by "kvm".
    # m -> monitor
    # km -> control
    mFrame = tk.CTkFrame(root)
    mFrame.grid(row=0,column=0)
    optionFrame = tk.CTkFrame(root)
    optionFrame.grid(row=0,column=1)

    mCanvas = tk.CTkCanvas(mFrame)
    mCanvas.pack(padx=10,pady=10)

    selectMachine = tk.CTkButton(optionFrame,text="Select machine")
    installationMediaSetting = tk.CTkButton(optionFrame,text="installation media")
    settingForGPUPaaThrough = tk.CTkButton(optionFrame,text="GPU pass through") # I want to add single GPU support.
    addDevice = tk.CTkButton(optionFrame,text="Add device")
    CtrlAltDelete = tk.CTkButton(optionFrame,text="Ctrl-Alt-Delete")
    AdvancedSetting = tk.CTkButton(optionFrame,text="Advanced setting")
    CtrlAltDelete.pack(padx=10,pady=10)
    selectMachine.pack(padx=10,pady=10)
    addDevice.pack(padx=10,pady=10)
    settingForGPUPaaThrough.pack(padx=10,pady=10)
    installationMediaSetting.pack(padx=10,pady=10)
    AdvancedSetting.pack(padx=10,pady=10)

window_name = "virtual machine with qemu"
root = tk.CTk()
root.title(window_name)

_prototype(root)

root.mainloop()