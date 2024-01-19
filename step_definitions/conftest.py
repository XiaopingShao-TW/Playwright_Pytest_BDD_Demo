# -*- coding:utf-8 -*-
import pytest
from page_object.search import Search


@pytest.fixture(scope='module')
def search_page(page):
    yield Search(page)
