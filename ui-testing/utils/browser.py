# coding: utf-8 
from selenium import webdriver
import os 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 


class Browser():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Browser()
        
        return cls.instance 
    
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        self._driver = webdriver.Chrome(os.path.join(os.getcwd(),"tests","thirdparty",'chromedriver.exe'),chrome_options=chrome_options)

    def get(self,url):
        self.get(url)


browser  = Browser.get_instance()