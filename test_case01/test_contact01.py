# -*- coding: utf-8 -*-
# @Author： Kid
# @FileName: test_contact01.py
from Web_Auto_Testing_Homework.page01.Main_page import MainPage


class TestContact:
    def setup(self):

        self.mainpage = MainPage()

    def test_addmembers(self):
        username = "Alice010"
        account = "alice0010"
        phone = "13200000010"

        pages = self.mainpage.goto_add_members()
        pages.add_members(username,account,phone)
        names = pages.get_members()
        print(names)
        assert username in names
