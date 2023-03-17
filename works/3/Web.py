from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import BaseWebElement
from webdriver_manager.chrome import ChromeDriverManager
import time
import threading

def _openWebSite(url = 'https://www.google.com/?hl=ja') -> webdriver.Chrome:
    driver = webdriver.Chrome(ChromeDriverManager().install())
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
    filename = title + " p tag content.txt"
    with open(filename,"w+",encoding="UTF-8") as textfile:
        for elem in WebElems:
            textfile.write(elem.text + "\n")

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


def countPTagCharFromURL(url:str):

    # url = "https://selenium-python.readthedocs.io/api.html?highlight=WebElement#selenium.webdriver.remote.webelement.WebElement.accessible_name"
    driver = _openWebSite(url)
    WebElems = _getPTagContent(driver)
    # th2 = threading.Thread(target=_outputToTextWebEelems,args=(WebElems,driver.title))
    # th2.start()
    return _countCharFromWebElems(WebElems)

time.sleep(31000)
# driver.quit()