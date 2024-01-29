import os
from config.conf import cm
from utils.tools import move_environment_file, generate_allure_report

# 切换到项目根目录
cmd = 'cd ' + cm.base_dir
os.system(cmd)
# 运行标签为smoke的测试用例集
cmd = 'pytest -v --gherkin-terminal-reporter -s --color=yes --alluredir=temp -m smoke'
os.system(cmd)
# 生成测试结果报告到report目录下
move_environment_file()
generate_allure_report()
