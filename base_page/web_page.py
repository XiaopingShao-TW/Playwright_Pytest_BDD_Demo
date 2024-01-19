# coding=utf-8
import os
import re
import allure
import random
from playwright.sync_api import expect
from config.conf import cm
from utils.logger import log


class WebPage(object):
    """
        Pyse framework for the main class, the original
    playwright provided by the method of the two packaging,
    making it easier to use.
    """

    def __init__(self, page):
        self.page = page

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Add any cleanup code here if needed
        pass

    def open(self, url):
        self.page.goto(url)
        log.info("成功打开网页：%s" % url)

    def get_element(self, css):
        return self.page.locator(css)

    def fill(self, css, content):
        self.get_element(css).fill(content)
        log.info("输入文本：{}".format(content))

    def click(self, css):
        self.get_element(css).click()
        log.info("点击元素：{}".format(css))

    def get_text(self, css):
        self.get_element(css).text_content()
        log.info("获取文本：{}".format(css))

    def element_to_be_visible(self, css):
        expect(self.get_element(css)).to_be_visible()
        log.info("可见元素：{}".format(css))

    def element_to_be_hidden(self, css):
        expect(self.get_element(css)).to_be_hidden()
        log.info("不可见元素：{}".format(css))

    def page_contain_title(self, content):
        # Expect a title "to contain" a substring.
        expect(self.page).to_have_title(re.compile(content))
        log.info("页面标题包含：{}".format(content))

    def page_contain_url(self, content):
        # Expects the URL to contain a substring.
        expect(self.page).to_have_url(re.compile(content))
        log.info("页面url包含：{}".format(content))

    def element_to_have_attribute(self, css, attribute, value):
        # Expect an attribute "to be strictly equal" to the value.
        expect(self.get_element(css)).to_have_attribute(attribute, value)
        log.info("元素包含属性：{}".format(attribute))

    def allure_png(self, name):
        """
        take screenshot  for allure report
        """
        st = random.randint(10000, 100000)
        s = name + str(st)
        file_path = os.path.join(cm.png_path, '{}.png'.format(s))  # 拼凑成需上传附件的绝对路径
        self.page.screenshot(path=file_path)
        allure.attach.file(file_path, s, allure.attachment_type.PNG)
        log.info("生成图片：{}".format(file_path))



