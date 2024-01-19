# -*- coding:utf-8 -*-
from base_page.web_page import WebPage
from utils.readconfig import ini
from utils.readelement import Element

search = Element('search')


class Search(WebPage):

    def __init__(self, page):
        super().__init__(page)

    def open_baidu_page(self):
        self.page.goto(ini.host)
        assert self.page.title() == "百度一下，你就知道"

    def input_key(self, content):
        self.fill(search['搜索输入框'], content)

    def click_search_btn(self):
        self.click(search['搜索按钮'])

    def verify_search_result(self, element):
        self.element_to_be_visible(search[element])
