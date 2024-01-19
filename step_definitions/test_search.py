import time
from pytest_bdd import scenario, given, when, then


@scenario('../features/search.feature', '百度搜索')
def test_search_function():
    pass


@given("打开百度首页")
def open_baidu(search_page):
    search_page.open_baidu_page()


@when("输入关键字<key_wd>进行搜索搜索")
def search_by_key_word(search_page, key_wd):
    search_page.input_key(key_wd)
    search_page.click_search_btn()


@then("进入搜索结果页面")
def search_result_page(search_page):
    search_page.verify_search_result('搜索结果')
    search_page.allure_png('搜索结果页面展示正常')
