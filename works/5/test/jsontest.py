import json
from tkinter import filedialog

def readJson():
    with filedialog.askopenfile("r") as file:
        reuslt = json.load(file)
        print(reuslt)

readJson()