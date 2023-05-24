from telnetlib import EC

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


def autoPublish():

    text1 = '2023年5月25日 天气晴  ｜   新鲜事早知道第073期'
    text2= '2023年5月25日 星期三 农历四月初六 今日科技与创新资讯推荐:'
    name_list = ['量子位', '华尔街见闻', '科技每日推送', '罗列思维', '云头条']

    url = 'https://mp.weixin.qq.com/cgi-bin/loginpage'
    # 输入驱动位置
    # driver = webdriver.Chrome('/Users/zhangxin/Downloads/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Edge('/Users/zhangxin/Downloads/chromedriver_mac_arm64/msedgedriver')
    # 打开网址
    driver.get(url)
    # 最大化浏览器窗口，更好的内容定位
    driver.maximize_window()
    print("打开微信公众平台，最大化窗口")

    ##选择已有图文消息
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/div/div[3]/div')))
    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[4]/div[2]/div/div[3]/div').click()
    print("点击选择已有图文按钮")
    # 打开新新页面， 展示已有图文
    driver.implicitly_wait(20)
    # WebDriverWait(driver, 50).until(ec.new_window_is_opened(driver.window_handles))
    driver.switch_to.window(driver.window_handles[1])
    print("切换到新窗口")
    # time.sleep(3)
    #选择第一个已有图文
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="appmsg_publish_record"]/div[1]/div/div/i')))
    driver.find_element(By.XPATH, '//*[@id="appmsg_publish_record"]/div[1]/div/div/i').click()
    print("选择第一个已有图文")
    # time.sleep(3)
    # 确定
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="vue_app"]/div[3]/div/div[1]/div/div[3]/div/div[1]/button')))
    driver.find_element(By.XPATH, '//*[@id="vue_app"]/div[3]/div/div[1]/div/div[3]/div/div[1]/button').click()
    print("选择第一个已有图文 》》点击确定按钮")
    time.sleep(10)

    # 进入文本区， 编辑文本信息
    # 时间1
    driver.switch_to.frame(driver.find_element(By.ID, 'ueditor_0'))
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '/html/body/section[1]/section/p[4]/span')))
    driver.find_element(By.XPATH, '/html/body/section[1]/section/p[4]/span').click()
    driver.find_element(By.XPATH, '/html/body/section[1]/section/p[4]/span').clear()
    driver.find_element(By.XPATH, '/html/body/section[1]/section/p[4]/span').send_keys(text1)
    print("编辑文本 》》 time 1")

    # 时间2
    WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.XPATH, '/html/body/section[1]/section/section/section/section/section[2]/p[2]/span')))
    driver.find_element(By.XPATH, '/html/body/section[1]/section/section/section/section/section[2]/p[2]/span').click()
    driver.find_element(By.XPATH, '/html/body/section[1]/section/section/section/section/section[2]/p[2]/span').clear()
    driver.find_element(By.XPATH, '/html/body/section[1]/section/section/section/section/section[2]/p[2]/span').send_keys(text2)
    print("编辑文本 》》 time 2")

    # #量子位、华尔街见闻、科技每日推送、罗列思维、云头条
    for index,name in enumerate(name_list):
        print("* * * * * * * * * * Start Article " + str(index + 1) + " * * * * * * * * * *")
        if index >= 1:
            # 进入文本区， 编辑文本信息
            WebDriverWait(driver, 30).until(ec.frame_to_be_available_and_switch_to_it((By.ID, 'ueditor_0')))
        # Xpath路径数值：4、6、8、10、12
        i = 4 + 2 * index
        xpath = '/html/body/section[1]/section/section/section/section/section[2]/p[' + str(i) + ']/a/span'
        WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, xpath)))
        driver.find_element(By.XPATH, xpath).click()
        driver.find_element(By.XPATH, xpath).clear()
        print('清除文章超链接')
        # 插入文章超链接
        link_insert(driver, name)
        print("编辑文本 》》 Success Article " + str(index + 1))

    #群发
    WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="js_send"]/button/span')))
    driver.find_element(By.XPATH, '//*[@id="js_send"]/button/span').click()
    print("群发")
    # 确认群发
    driver.switch_to.default_content()
    WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="vue_app"]/div[3]/div[1]/div[1]/div/div[3]/div/div[2]/div/button')))
    driver.find_element(By.XPATH, '//*[@id="vue_app"]/div[3]/div[1]/div[1]/div/div[3]/div/div[2]/div/button').click()
    print("确认群发")
    #继续群发
    driver.switch_to.default_content()
    WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="vue_app"]/div[3]/div[2]/div[1]/div/div[3]/div/div[1]/button')))
    driver.find_element(By.XPATH, '//*[@id="vue_app"]/div[3]/div[2]/div[1]/div/div[3]/div/div[1]/button').click()
    print("发布成功 ！！！")
    time.sleep(20)

def link_insert(driver, name):
    # 点击超链接
    driver.switch_to.default_content()
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.ID, 'js_editor_insertlink')))
    driver.find_element(By.ID, 'js_editor_insertlink').click()
    print("点击超链接按钮")
    # 选择其它公众号
    driver.switch_to.default_content()
    # 点击选择其他公众号
    WebDriverWait(driver, 30).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/p/div/button')))
    driver.find_element(By.XPATH,'//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/p/div/button').click()
    print("点击选择其他公众号按钮")
    # 输入公众号名称
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div/div[1]/span/input')))
    driver.find_element(By.XPATH, '//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div/div[1]/span/input').send_keys(name)
    print("输入公众号名称: " + name)
    # 进行查询公众号
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div/div[1]/span/input')))
    driver.find_element(By.XPATH, '//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div/div[1]/span/input').send_keys(Keys.ENTER)
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div[2]/ul/li[1]')))
    driver.find_element(By.XPATH,'//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[4]/div/div/div/div[2]/ul/li[1]').click()
    print("选择公众号")
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[5]/div/div/div[2]/div/div/label[1]/span[1]/label/i')))
    driver.find_element(By.XPATH,'//*[@id="vue_app"]/div[3]/div[1]/div/div[2]/div[2]/form[1]/div[5]/div/div/div[2]/div/div/label[1]/span[1]/label/i').click()
    print("选择公众号最新文章")
    # 完成
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="vue_app"]/div[3]/div[1]/div/div[3]/button')))
    driver.find_element(By.XPATH, '//*[@id="vue_app"]/div[3]/div[1]/div/div[3]/button').click()



if __name__ == '__main__':
    autoPublish();