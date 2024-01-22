from playwright.sync_api import sync_playwright
import pytest
from config.conf import cm
from utils.tools import ini_file_dic


@pytest.fixture(scope='module')
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(
            ignore_https_errors=True,
            viewport={
                "width": 1920,
                "height": 1040,
            }
        )
        page = context.new_page()
        yield page
        context.close()
        page.close()


@pytest.fixture(scope='session', autouse=True)
def setup():
    # 测试执行之前初始化文件目录temp, report, picture
    ini_file_dic(cm.temp_path)
    ini_file_dic(cm.report_path)
    ini_file_dic(cm.png_path)

