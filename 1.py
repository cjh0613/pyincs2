import configparser
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



def main():
    print('''
峡州仙士Gitee Page一键自动部署官方发布地址：
    https://cjh0613.github.io/blog/20200511GiteePageAuto.html
转载请遵守 BY-NC-SA 许可协议 ，注明出处！
开始运行……
（若无法成功自动部署请检查配置文件及网络连接）
    ''')
    time_start=time.time()
    options=Options()
    options.binary_location = "./chrome/chrome.exe"
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    driver=webdriver.Chrome(executable_path="./chrome/chromedriver.exe",chrome_options=options)
    #  实例化configParser对象
    config = configparser.ConfigParser()
    # -read读取ini文件
    config.read('config.ini', encoding='UTF-8')
    #browser =driver
    driver.get("https://gitee.com/"+config.get('config', 'userName')+"/"+config.get('config', 'repoName')+"/pages")
    condition = expected_conditions.visibility_of_element_located((By.ID, 'navbar-search-input'))
    WebDriverWait(driver=driver, timeout=20, poll_frequency=0.5).until(condition)
    time.sleep(0.5)
    driver.find_element(By.LINK_TEXT, "登录").click()
    condition = expected_conditions.visibility_of_element_located((By.ID, 'user_login'))
    WebDriverWait(driver=driver, timeout=20, poll_frequency=0.5).until(condition)
    driver.find_element(By.ID, "user_login").click()
    driver.find_element(By.ID, "user_login").send_keys(config.get('config', 'loginName'))
    time.sleep(0.5)
    driver.find_element(By.ID, "user_password").click()
    driver.find_element(By.ID, "user_password").send_keys(config.get('config', 'passWord'))
    time.sleep(0.5)
    driver.find_element(By.NAME, "commit").click()
    
    if config.get('config', 'pullGithub')=='1':
        condition = expected_conditions.visibility_of_element_located((By.ID, 'btn-sync-from-github'))
        WebDriverWait(driver=driver, timeout=20, poll_frequency=0.5).until(condition)
        driver.find_element(By.ID, "btn-sync-from-github").click()
        time.sleep(10)
        try:
            driver.find_element_by_xpath('//*[@id="modal-sync-from-github"]/div[3]/div[3]').click()
            print('Gitee Page 从Github同步成功，耗时')
            cjhCost=str(int((time.time()-time_start)/60))+':'+str(int((time.time()-time_start)%60))
            print([cjhCost])
            # 等待5秒更新
            time.sleep(5)
        except:
            date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            print('''
    gitee同步出错！请速处理！
    ''')
    elif config.get('config', 'pullGithub')=='0':
        time.sleep(5)
        try:
            # 点击更新按钮--通过xpath确定点击位置/html/body/div[3]/div[2]/div/div[2]/div[1]/form/div[7]
            driver.find_element_by_xpath('//*[@id="pages-branch"]/div[7]').click()
            # 确认更新提示框--这个函数的作用是确认提示框
            Alert(driver).accept()

            # 等待5秒更新
            time.sleep(5)

            # 这个print其实没事什么用,如果真的要测试脚本是否运行成功，可以用try来抛出异常
            print("Gitee Page Deploy成功，耗时")
            cjhCost=str(int((time.time()-time_start)/60))+':'+str(int((time.time()-time_start)%60))
            print([cjhCost])
        except:
            date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            print('''
    gitee deploy出错！请速处理！
    ''')
    else:
         print('''
    pullGithub 参数设置不正确！请速处理！
    ''')
    driver.quit()
main()

