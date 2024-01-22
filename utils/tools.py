import os
import platform
import shutil
import stat
from config.conf import cm
from utils.logger import log


def get_sys():
    return platform.system().lower()


def ini_file_dic(ini_path):
    if get_sys() == 'windows':
        os.system('rd /s/q %s' % ini_path)
    else:
        os.system('rm -rf %s' % ini_path)
    os.mkdir(ini_path)
    os.chmod(ini_path, stat.S_IRWXG)
    os.system('sudo chmod -R 777 %s' % ini_path)


def move_environment_file():
    shutil.copyfile(cm.allure_env_config, os.path.join(cm.temp_path, 'environment.properties'))
    log.info('复制allure配置文件到temp目录下用来在allure report中展示')


def generate_allure_report():
    test_result = cm.temp_path
    test_report = cm.report_path
    if get_sys() == 'windows':
        allure_pkg = os.path.join(cm.base_dir, 'allure', 'bin', 'allure.bat')
        win_cli = '{} generate {} -o {} --clean'.format(allure_pkg, test_result, test_report)
        log.info(os.popen(win_cli).read())
    else:
        allure_pkg = os.path.join(cm.base_dir, 'allure', 'bin', 'allure')
        mac_cli = 'chmod a+x %s;%s generate %s -o %s --clean' % (allure_pkg, allure_pkg, test_result, test_report)
        log.info(os.popen(mac_cli).read())
    log.info('生成allure测试报告')