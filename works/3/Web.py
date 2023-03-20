from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading
from tkinter import filedialog


def _IsChromeDriverWorking():
    driver = webdriver.Chrome(ChromeDriverManager().install())

def _openWebSite(url = 'https://www.google.com/?hl=ja') -> webdriver.Chrome:
    option = Options()
    option.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=option)
    driver.get(url)
    return driver

def _changeWindowSize(width,height,driver: webdriver.Chrome):
    driver.set_window_size(width,height)

def _getPTagContent(driver: webdriver.Chrome):
    WebElems = driver.find_elements(By.TAG_NAME,"p")
    return WebElems

def _PrintCharacterFromWebElem(WebElems):
    for elem in WebElems:
        print(elem.text)

def _outputToTextWebEelems(WebElems,title):
    filename = "p tag content.txt"
    path = filedialog.askdirectory()
    if(0 == len(path)):
        pass
    else:
        path += "/"
    filenameAndPath = path + filename
    with open(filenameAndPath,"w+",encoding="UTF-8") as textfile:
        for elem in WebElems:
            textfile.write(elem.text + "\n")

# ---------------------------------------------------------------

def _countCharFromStr(strings:str) -> int:
    count = 0
    for char in strings:
        count += 1
    return count

def _countCharFromWebElems(WebElems) -> int:
    count = 0
    for elem in WebElems:
        count +=_countCharFromStr(elem.text)
    return count

# ------------------------------------------

def getAnyTagNameOfContent(driver,tagname:str):
    WebElems = driver.find_elements(By.TAG_NAME,tagname)
    return WebElems

def getAllTag(driver):
    driver:webdriver.Chrome
    WebElems = driver.find_elements(By.TAG_NAME,"*")
    return WebElems


def countPTagCharFromURL(url:str):

    # url = "https://selenium-python.readthedocs.io/api.html?highlight=WebElement#selenium.webdriver.remote.webelement.WebElement.accessible_name"
    driver = _openWebSite(url)
    WebElems = _getPTagContent(driver)
    # th2 = threading.Thread(target=_outputToTextWebEelems,args=(WebElems,driver.title))
    # th2.start()
    return _countCharFromWebElems(WebElems),driver.title


# driver.quit()
if __name__ == "__main__":
    # _IsChromeDriverWorking()

    # This is working!
    def asterriskTagNameTest():
        driver = _openWebSite("https://ejje.weblio.jp/content/modify")
        elems = getAllTag(driver)
        # _PrintCharacterFromWebElem(elems)
        _outputToTextWebEelems(elems,driver.title)

    asterriskTagNameTest()
