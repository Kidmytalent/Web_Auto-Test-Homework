# -*- coding: utf-8 -*-
# @Author： Kid
# @FileName: add_members.py
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Web_Auto_Testing_Homework.page01.Base_page import BasePage


class AddMembersPage(BasePage):

    def add_members(self,username,account,phone):
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(account)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()  #  class-id 查询结果有上下两个,从上往下查找，默认第一个
        return True

    def get_members(self):
        locator = (By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        self.wait_to_load(10, locator)
        element_list = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        names = []
        for element in element_list:
            names.append(element.get_attribute("title"))
        return names
