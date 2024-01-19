#!/usr/bin/python
# -*- coding: utf-8 -*-
Feature: 百度搜索
  @smoke
  Scenario Outline: 百度搜索
    Given 打开百度首页
    When 输入关键字<key_wd>进行搜索搜索
    Then 进入搜索结果页面
    Examples:
      | key_wd |
      | 自动化 |
      | 学习 |



