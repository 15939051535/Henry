#coding=utf-8

'''定位单个元素封装'''

# APPLICATION_PATH = ('C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\邮掌柜.exe')  #定义邮掌柜路径
# login_url = ("file:\\C:\\Program Files (x86)\\UleSoft\\邮掌柜4\\face\\_modules_\\login\\login.html") #定义登录页面file文件路径

# options = webdriver.ChromeOptions()
# options.binary_location = APPLICATION_PATH

#写死打开邮掌柜的路径
# def __init__(self, driver):
#     self.driver = webdriver.Chrome(chrome_options=options)
#     self.driver = driver

#写死启动浏览器
# def __init__(self, driver):
#     启动浏览器参数化
#     # self.driver = webdriver.Firefox()
#     self.driver = driver

# def open(self, url):
#     '''
#     使用get打开url后，最大化窗口，判断title符合预期
#     '''
#     self.driver.get(url)
#     self.driver.maximize_window()


#浏览器初始化，不写死
def __init__(self, driver):
    self.driver = driver







def findId(driver,id):
    f = driver.find_element_by_id(id)
    return f

def findName(driver,name):
    f = driver.find_element_by_name(name)
    return f

def findClassName(driver,name):
    f = driver.find_element_by_class_name(name)
    return f

def findTagName(driver,name):
    f = driver.find_element_by_tag_name(name)
    return f

def findLinkText(driver,text):
    f = driver.find_element_by_link_text(text)
    return f

def findPLinkText(driver,text):
    f = driver.find_element_by_partial_link_text(text)
    return f

def findXpath(driver,xpath):
    f = driver.find_element_by_xpath(xpath)
    return f

def findCss(driver,css):
    f = driver.find_element_by_css_selector(css)
    return f

'''定位一组元素封装'''

def findsId(driver,id):
    f = driver.find_elements_by_id(id)
    return f

def findsName(driver,name):
    f = driver.find_elements_by_name(name)
    return f

def findsClassName(driver,name):
    f = driver.find_elements_by_class_name(name)
    return f

def findsTagName(driver,name):
    f = driver.find_elements_by_tag_name(name)
    return f

def findsLinkText(driver,text):
    f = driver.find_elements_by_link_text(text)
    return f

def findsPLinkText(driver,text):
    f = driver.find_elements_by_partial_link_text(text)
    return f

def findsXpath(driver,xpath):
    f = driver.find_elements_by_xpath(xpath)
    return f

def findsCss(driver,css):
    f = driver.find_elements_by_css_selector(css)
    return f
