from selenium import webdriver
import unittest
import time

'''入门的自动化测试工程师，登录自动化测试用例'''


class Test(unittest.TestCase):
    def testcase01(self):
        '''用例1'''
        browser = webdriver.Chrome()  # 打开浏览器
        browser.get("http://47.94.172.18/signin")  # 访问测试项目网站
        browser.find_element_by_xpath("/html/body/form/p[1]/input").send_keys('15902127953')  # 输入用户名
        browser.find_element_by_xpath("//html/body/form/p[2]/input").send_keys('123456')  # 输入用户名
        time.sleep(3)
        browser.find_element_by_xpath("/html/body/form/p[3]/button").click()  # 点击登录
        # 断言
        use = browser.find_elements_by_xpath("//*[text()='welcome15902127953']")
        self.assertEqual(len(use), 1)
        # if use.is_displayed():
        #     print('登录成功')
        # else:
        #     print('登录失败')

    def testcase02(self):
        '''用例2'''
        browser = webdriver.Chrome()  # 打开浏览器
        browser.get("http://47.94.172.18/signin")  # 访问测试项目网站
        browser.find_element_by_xpath("/html/body/form/p[1]/input").send_keys('15902127953')  # 输入用户名
        browser.find_element_by_xpath("//html/body/form/p[2]/input").send_keys('123456')  # 输入用户名
        browser.find_element_by_xpath("/html/body/form/p[3]/button").click()  # 点击登录


if __name__ == '__main__':
    unittest.main()
