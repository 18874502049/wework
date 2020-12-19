from selenium import webdriver
import yaml
import time
# chrome --remote-debugging-port=9222  浏览器的复用
# 然后在打开的浏览器中输入 127.0.0.1:9222
# class TestWework:
  # 复用浏览器
  # def test_demo(self):
  #   opt = webdriver.ChromeOptions()
  #   # 设置debug地址
  #   opt.debugger_address = '127.0.0.1:9222'
  #   driver = webdriver.Chrome(options=opt)
  #   driver.implicitly_wait(5)
  #   driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
  #   driver.find_element_by_id("menu_contacts").click()
  #   print(driver.get_cookies())

# 使用cookie登录
# def test_cookie():
#   driver = webdriver.Chrome()
#   driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
#   driver.implicitly_wait(5)
#   cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'cKm8Kdp_aUyeX4LQ-2EJm0MrHhcB2Ilutn6M7QiXOkzHTAR9UueB3qsUJLmipno8O068pEoO5xq6izRXDuXfDc4dTOCTyLn-mofi2YxHDcPKzXeQQEokxJBpe7PceGrWXqlHjDVOOUonQ25FYb6SwKptM1ezUCdZ0Ho5M-6TVAULF2kuMrDjrcEzvy2q_QdEpT0mXcnWCgjOukF6Gnm3XzVanrjQrJBedoeyXbS4k8FdClEcoMvM0audRcUTPlMmuV2SKLsPyfFj7HlMeOZppQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'w5TOPE_sHjnnV3TOXfZm_dYWkKdzFu5XydvnNrRJfGrI_V4ux1D4Ev2Mwnbx77AE'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608388588'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853131883955'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1608388732, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': 'work.weixin.qq.com', 'expiry': 1608419240, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '7e48ft8'}, {'domain': '.qq.com', 'expiry': 1671460606, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1710546747.1608206624'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853131883955'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'a77ce7829dd1f0232271750ccb9e07c72eceb3e4756f8de593064ec6f814199b'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639742547, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1608475006, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1215303770.1608387730'}, {'domain': '.work.weixin.qq.com', 'expiry': 1610980613, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7419658'}, {'domain': '.work.weixin.qq.com', 'expiry': 1639924587, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1608206623,1608387728,1608388426,1608388588'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '27045328561303656'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'ZqBV/HiHEf'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325081207805'}, {'domain': '.qq.com', 'expiry': 1921736282, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_28cfe539e3be7'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '7038737054'}]
#   for cookie in cookies:
#     driver.add_cookie(cookie)
#   driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
#   driver.find_element_by_id("menu_contacts").click()
#   time.sleep(5)

def test_get_cookie():
  opt = webdriver.ChromeOptions()
  # 设置debug地址
  opt.debugger_address = '127.0.0.1:9222'
  driver = webdriver.Chrome(options=opt)
  driver.implicitly_wait(5)
  driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
  cookie = driver.get_cookies()
  print(cookie)
  with open("data.yaml","w",encoding="UTF-8") as f:
    yaml.dump(cookie,f)

# 使用序列化cookie的方法进行登录
def test_login():
  driver = webdriver.Chrome()
  driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
  driver.implicitly_wait(5)
  with open("data.yaml",encoding="UTF-8") as f:
    yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
      driver.add_cookie(cookie)
  driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
  time.sleep(2)
  driver.find_element_by_link_text("添加成员").click()
  driver.find_element_by_id("username").send_keys("小红")
  driver.find_element_by_id("memberAdd_english_name").send_keys("小红")
  name = driver.find_element_by_id("memberAdd_english_name").get_attribute("value")
  driver.find_element_by_id("memberAdd_acctid").send_keys("xiaohong")
  driver.find_elements_by_name("gender")[1].click()
  driver.find_element_by_id("memberAdd_phone").send_keys("15644564542")
  driver.find_element_by_id("memberAdd_telephone").send_keys("0755-88888888")
  driver.find_element_by_id("memberAdd_mail").send_keys("347389232@qq.com")
  driver.find_element_by_id("memberEdit_address").send_keys("广东深圳")
  driver.find_element_by_id("memberAdd_title").send_keys("软件测试工程师")
  driver.find_element_by_link_text("保存并继续添加").click()
  assert name == '小红'
  time.sleep(10)