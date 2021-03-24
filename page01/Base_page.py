# -*- coding: utf-8 -*-
# @Author： Kid
# @FileName: Base_page.py

#  基类封装
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ""
    def __init__(self,driver:WebDriver=None):
        if driver == None:       #  如果 driver 为空，则实例化driver，并复用启动浏览器

            option=Options()
            option.debugger_address="127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(5)

        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self, locator, value):
        return self.driver.find_element(locator, value)
    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)
    def wait_to_load(self,timeout,locator):
        WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable((locator)))


