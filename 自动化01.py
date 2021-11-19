from selenium import  webdriver
import time
# 创建一个谷歌浏览器
driver = webdriver.Chrome()

# 打开一个网址
# driver.get("https://www.jd.com/")
#
# # 最大化
# driver.maximize_window()
#
# driver.find_element_by_id("key").send_keys("thinkpad")
#
# driver.find_element_by_xpath("//*[@class='button']").click()
#
# time.sleep(5)
# driver.find_element_by_xpath("//*[@data-sku='100020733038']").click()
# driver.switch_to.window(driver.window_handles[-1])
# time.sleep(5)
# driver.find_element_by_xpath("//*[@class='btn-add']").click()
# time.sleep(5)
# driver.find_element_by_id('InitCartUrl').click()



# driver.get("https://www.suning.com/")
#
# # 最大化
# driver.maximize_window()
# time.sleep(5)
# driver.find_element_by_id("searchKeywords").send_keys("thinkpad")
#
# driver.find_element_by_xpath("//*[@class='search-btn btn-new']").click()
#
# time.sleep(3)
#
# time.sleep(5)
# driver.find_element_by_id("0010327863-12298274940").click()
# time.sleep(5)
# driver.switch_to.window(driver.window_handles[-1])
# driver.find_element_by_id('addCart').click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@class='go-cart']").click()
# time.sleep(2)
# driver.find_element_by_xpath("//*[@class='cart-btn login-btn']").click()
#



driver.get("https://www.bilibili.com/")

# 最大化
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath("//*[@class='nav-search-keyword']").send_keys("萨 日 朗")

driver.find_element_by_xpath("//*[@class='nav-search-btn']").click()

time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
driver.find_element_by_xpath("//*[@title='⚡萨 日 朗！！！⚡']").click()

driver.switch_to.window(driver.window_handles[-1])
time.sleep(5)
driver.find_element_by_xpath("//*[@class='like']").click()
