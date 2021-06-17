from selenium import webdriver
from selenium.webdriver.common.by import By

from test_wechat_po.package.basepage import BasePage
from test_wechat_po.package.contact_page import Contact

# 首页
class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_contact(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.find_element_by_id("menu_contacts").click()
        self.find_and_click(By.ID,"menu_contacts")
        return Contact(self.driver)