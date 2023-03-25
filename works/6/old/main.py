from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import filedialog
import time
import random
from tkEntry import value
import sys

ins = value()
URL = ins.result
if URL == "":
    sys.exit()

script = "window.scrollBy(0,50000)"


options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.set_window_size(3000,3000)

driver.get(URL)


amount = 100
waitTime = 1 # s
for index in range(amount):
    driver.execute_script(script)
    waitTime = random.randint(1,3)
    time.sleep(waitTime)


elems = driver.find_elements(By.TAG_NAME,"img")

# elems[1].get_attribute("src")

# from tkinter import filedialog
path = filedialog.askdirectory() + "/"
# print(path)

for index,img in enumerate(elems):
    try:
        if img.get_attribute("src"):
            with open(path + str(index) + ".png","wb") as file:
                file.write(img.screenshot_as_png)
    except:
        pass



