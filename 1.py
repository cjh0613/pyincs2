import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def CJHrandomS():
    s1=random.choice(['宜昌','宜昌市','湖北省宜昌市','湖北宜昌','湖北省宜昌','湖北宜昌市','三峡大学'])
    a1=random.choice(['',' ','  '])
    s2=random.choice(['八中','8中','八中','第八中学','第八中','三峡大学附属中学','三峡大学附中'])
    a2=random.choice(['',' ',' ',' ','  '])
    s3=random.choice(['官网','官方网站',])
    s=s1+a1+s2+a2+s3
    return s
    
def main():
    global driver
    try:
        options=Options()
        options.binary_location = "./chrome/chrome.exe"
        options.executable_path="./chrome/chromedriver.exe"
        #options.binary_location = r"D:\mypro\Panda_learning-32\chrome\chrome.exe"
        options.add_argument('--window-size=1920,1080')
        #options.add_argument('--headless')
        options.add_argument('lang=zh_CN.UTF-8')
        u1=random.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        # Opera
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        # Firefox
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        # Safari
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        # chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        # 360
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        # 淘宝浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        # 猎豹浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        # QQ浏览器
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        # sogou浏览器
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        # maxthon浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        # UC浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36"])
        UserAgent = u1
        options.add_argument('User-Agent=' + UserAgent)
        time_start=time.time()
        driver=webdriver.Chrome(options=options)
        #driver=webdriver.Chrome(options=options)
        driver.get("http://www.baidu.com")
        #browser =driver

        #driver.get("https://www.baidu.com/baidu?wd=宜昌八中官网&ie=utf-8")
        s1=random.choice(['宜昌','宜昌市','湖北省宜昌市','湖北宜昌','湖北省宜昌','湖北宜昌市','三峡大学'])
        a1=random.choice(['',' ','  '])
        s2=random.choice(['八中','8中','八中','第八中学','第八中','三峡大学附属中学','三峡大学附中'])
        a2=random.choice(['',' ',' ',' ','  '])
        s3=random.choice(['官网','官方网站',])
        s=s1+a1+s2+a2+s3
        # 获取输入框标签对象
        element = driver.find_element_by_id('kw')
        # 输入框输入内容
        element.send_keys(s)
        element.send_keys(Keys.ENTER)
        condition = expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "https://cjh0613.gitee.io"))
        WebDriverWait(driver=driver, timeout=15, poll_frequency=1).until(condition)
        try:

            #driver.findElement(By.xpath("//*[@id="+n+"]/div[2]/a[1][contains(text(),'cjh0613.gitee.io')]"))
            driver.find_element_by_partial_link_text("https://cjh0613.gitee.io").click()
            print ('test pass: element found by link text')
            time.sleep(10)
        except:
            try:
                driver.find_element_by_xpath('//*[@id="page"]/a[1]').click()
                condition = expected_conditions.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "https://cjh0613.gitee.io"))
                WebDriverWait(driver=driver, timeout=7, poll_frequency=1).until(condition)
                driver.find_element_by_partial_link_text("https://cjh0613.gitee.io").click()
                time.sleep(5)
            except:
                print ("Exception found")
    except:
        print('fail')
    driver.quit()

i=1
time_start=time.time()
while 1:
    main()
    print([str(int((time.time()-time_start)/60))+':'+str(int((time.time()-time_start)%60))])
    print('次数：'+str(i))
    i=i+1

