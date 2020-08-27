#必应 峡州仙士之页
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def main():
    global j
    #try:
    options=Options()
    options.binary_location = "./chrome/chrome.exe"
    #options.executable_path="./chrome/chromedriver.exe"
    #options.binary_location = r"D:\mypro\Panda_learning-32\chrome\chrome.exe"
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--headless')
    options.add_argument('log-level=3')#禁用打包的命令行界面大量日志信息滚动输出INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
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
    driver=webdriver.Chrome(executable_path="./chrome/chromedriver.exe",options=options)
    cjhkeywords=getHTMLText('https://0a.cjh0613.com/cjh0613_com_seo/keywords_sogou.html')
    #driver=webdriver.Chrome(options=options)
    updata_log = cjhkeywords.split("\n")
    url =updata_log[6].split("=")[1].split(",")
    driver.get(random.choice(url))
    #browser =driver
    if cjhkeywords=='':
        print('获取设置失败')
        time.sleep(300)
        driver.quit()
    elif updata_log[0].split("=")[1]=='0':
        print('关闭')
        driver.quit()
        time.sleep(1800)
    else:

        #driver.get("https://www.baidu.com/baidu?wd=宜昌八中官网&ie=utf-8")
        s1=random.choice(updata_log[1].split("=")[1].split(","))
        a1=random.choice(updata_log[2].split("=")[1].split(","))
        s2=random.choice(updata_log[3].split("=")[1].split(","))
        a2=random.choice(updata_log[4].split("=")[1].split(","))
        s3=random.choice(updata_log[5].split("=")[1].split(","))
        s=s1+a1+s2+a2+s3
        print(s)
        # 获取输入框标签对象
        search_input = updata_log[7].split("=")[1].split(",")[0]
        if search_input=='id':
            element = driver.find_element_by_id(updata_log[8].split("=")[1].split(",")[0])
        else:
            element = driver.find_element_by_xpath(updata_log[9].split("=")[1].split(",")[0])
        # 输入框输入内容
        element.send_keys(s)
        element.send_keys(Keys.ENTER)
        condition = expected_conditions.visibility_of_element_located((By.XPATH, updata_log[10].split("=")[1]))
        print(updata_log[10].split("=")[1])
        try:
            tag1=0
            WebDriverWait(driver=driver, timeout=15, poll_frequency=1).until(condition)
            print('发现元素！')
        except:
            print('没有发现元素！')
            driver.quit()
            tag1=1
        try:

            driver.find_element_by_xpath(updata_log[11].split("=")[1]).click()
            #driver.find_element_by_partial_link_text("https://cjh0613.").click()
            print ('成功点击！！！——————test pass: element found by link text')
            j=j+1
            print([str(int((time.time()-time_start)/60))+':'+str(int((time.time()-time_start)%60))])
            print(str(int(j / i * 100))+'%    '+'成功次数：'+str(j)+'    总次数：'+str(i))
            cjht=random.choice(updata_log[12].split("=")[1].split(","))
            print('等待'+cjht)
            time.sleep(int(cjht))
            if tag1==0:
                driver.quit()
        except:
            print ("点击失败！")
            if tag1==0:
                driver.quit()
#except:
    #print('fail')
    #driver.quit()

i=1
j=0
time_start=time.time()
while 1:
    main()
    print([str(int((time.time()-time_start)/60))+':'+str(int((time.time()-time_start)%60))])
    print(str(int(j / i * 100))+'%    '+'成功次数：'+str(j)+'    总次数：'+str(i))
    i=i+1
