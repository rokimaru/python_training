# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from application import Application
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="test", header="test", footer="test"))
        self.logout()

    def test_add_empty_group(self):
        self.login(username="admin", password="secret")
        self.create_group(Group(name="", header="", footer=""))
        self.logout()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
