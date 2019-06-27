# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def fanya():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.maximize_window()

    dcap = dict(DesiredCapabilities.PHANTOMJS)

    dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")

    handles = (driver.window_handles)  # 获取当前窗口句柄集合（列表类型）
    print (handles)  # 输出句柄集合
    time.sleep(2)

    try:
        driver.switch_to.window(handles[1])
        driver.close()

        driver.switch_to.window(handles[0])

        driver.get('https://my.chzu.edu.cn/zfca/login')

        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys('xxx')#账号
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys('xxx')#密码

        driver.find_element_by_xpath('//*[@id="thetable"]/div[8]/span[1]/input[3]').click()
        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="141283777286462954"]/h5').click()
        time.sleep(3)

        handles = (driver.window_handles)  # 获取当前窗口句柄集合（列表类型）
        print (handles)  # 输出句柄集合
        driver.switch_to.window(handles[1])
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/a').click()
        time.sleep(5)

        handles = (driver.window_handles)  # 获取当前窗口句柄集合（列表类型）
        print (handles)  # 输出句柄集合

        time.sleep(1)
        driver.switch_to.window(handles[0])
        time.sleep(1)
        driver.close()
        driver.switch_to.window(handles[1])
        time.sleep(1)
        driver.close()

        driver.switch_to.window(handles[2])

        driver.get('http://mooc1-1.chaoxing.com/visit/courses')

        driver.find_element_by_link_text('移动应用开发').click()
        driver.find_element_by_link_text('Java EE应用开发').click()
        driver.find_element_by_link_text('无线网络').click()
        time.sleep(2)

        handles = (driver.window_handles)  # 获取当前窗口句柄集合（列表类型）
        print (handles)  # 输出句柄集合
        #移动应用开发
        driver.switch_to.window(handles[1])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/li[6]/a').click()
        time.sleep(1)
        driver.get_screenshot_as_file('wuxianzuoye.png')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/ul/li[7]/a').click()
        time.sleep(1)
        driver.get_screenshot_as_file('wuxiankaoshi.png')

        #Javaee
        driver.switch_to.window(handles[2])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/li[6]/a').click()
        time.sleep(1)
        driver.get_screenshot_as_file('javaeezuoye.png')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/ul/li[7]/a').click()
        time.sleep(1)
        driver.get_screenshot_as_file('javeeekaoshi.png')

        #无线网络
        driver.switch_to.window(handles[3])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/li[6]/a').click()
        time.sleep(1)
        driver.get_screenshot_as_file('androidzuoye.png')
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/ul/li[7]/a').click()
        time.sleep(1)
        driver.get_screenshot_as_file('androidkaoshi.png')

    except :
        print("非正常结束")

    finally:
        driver.quit()


def ahmooc():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()

        dcap = dict(DesiredCapabilities.PHANTOMJS)

        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36")

        driver.get('http://www.ahmooc.cn/login')
        time.sleep(2)

        driver.find_element_by_id('user_name').clear()
        driver.find_element_by_id('user_name').send_keys('xxxx')  #账号

        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys('xxxx')   #密码

        driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(2)

        driver.find_element_by_xpath(
            '/html/body/div[1]/div[4]/div/div[3]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/a').click()
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=100000"
        driver.execute_script(js)
        time.sleep(3)
        driver.get_screenshot_as_file('ahmooc.png')

    except:
        print("ahmooc非正常错误")

    finally:
        driver.quit()

if __name__ == '__main__':
    fanya()

    ahmooc()