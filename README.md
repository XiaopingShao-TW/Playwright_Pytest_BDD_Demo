
# 项目介绍
Pytest + Playwright + Allure UI自动化demo
目前有的功能：
- UI自动化POM设计模式 
- Playwright 的基本功能封装（打开网页，元素定位，元素操作，断言） 
- Pytest fixture 常见的使用方式
- Pytest 命令行各种常用的参数配置
- Allure 报告用github page的
- 支持logs封装


# 项目结构 📚
```text
├── allure                     # 📂 allure包
├── base_page                  # 📂 playwright基本功能进一步封装
├── config                     
│   ├── conf.py                # 🔧 项目目录及文件地址
│   └── config.ini             # 🧪 被测系统相关的配置
├── features                   # 📂 测试特性描述文件
├── file                       # 📂 测试截图文件
├── logs                       # 📂 存放日志的文件夹
├── README.md                  # 📝 项目介绍及使用指南
├── temp                       # 📊 Allure测试结果存放目录                  
├── logs                       # 📂 存放日志的文件夹
├── page_object                # 📑 页面类文件夹，按Page Object设计模式划分
│   └── search.py              # 🔐 百度搜索脚本
├── page_element               # 📑 页面元素存放目录
├── pytest.ini                 # ⚙️ pytest配置文件
├── pipfile                    # 📃 项目依赖文件
├── step_definitions           # 📁 测试用例文件夹
│   ├── conftest.py            # 🔧 存放pytest的fixture
│   └── test_search.py         # 🧪 测试用例页面用例
├── report                     # 📁 测试报告存放目录
├── utils                      # 📁 读取配置文件及公共方法封装的目录
├── run.py                     # 📁 执行测试的脚本
```
 

# 快速开始 ⏩
## 环境准备 🛠️
- Python 3.8
- 环境用的是pipenv来管理的：
 - 如果是自主安装搭建环境Pytest + Playwright + Allure + BDD环境，可以参考pipfile中的依赖逐一进行安装， [安装参考](https://www.jianshu.com/p/8fff583ccb5b) 🎈
 - 如果直接是下载本项目进行搭建，安装好pipenv后可以直接安装依赖：pipenv install （会自动安装pipfile中的所有依赖）

## 安装浏览器 🌐
```shell
playwright install
```

## 运行测试并生成报告 🚀
```shell
python run.py
```
