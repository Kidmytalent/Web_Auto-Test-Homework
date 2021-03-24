# -*- coding: utf-8 -*-
# @Author： Kid
# @FileName: Main_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Web_Auto_Testing_Homework.page01.Base_page import BasePage
from Web_Auto_Testing_Homework.page01.add_members import AddMembersPage


class MainPage(BasePage):

    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"   # 打开首页

    def goto_add_members(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()    # 遇到网页上面的功能或服务 有 类似 多个相同功能框框的点击按钮时就要注意在 调用谷歌定位分析时 会有 父节点和兄弟节点的问题，而且如果不分析兄弟节点问题，定位元素的id也不唯一，是不能使用的
        return AddMembersPage(self.driver)
