# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://www.bobbywade.com/")
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("2.WORK EXPERIENCE")).perform()
    wd.find_element_by_link_text("2.WORK EXPERIENCE").click()

    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("work-experience")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='work-experience']/div/div/div[1]/h2")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("h3")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='work-experience']//p[.='Sensus']")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='work-experience']/div/div/div[2]/p[3]")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.cv-item")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("h3")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.cv-item")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='work-experience']/div/div/div[1]/h2")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("work-experience")).perform()

    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='nav']/div/div")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("3.TECHNICAL SKILLS")).perform()
    wd.find_element_by_link_text("3.TECHNICAL SKILLS").click()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("menu")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("2.WORK EXPERIENCE")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("menu")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("1.PERSONAL INFO")).perform()
    wd.find_element_by_link_text("1.PERSONAL INFO").click()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='nav']/div/div")).perform()

    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("work-experience")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.cv-item")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='work-experience']//p[.='Sensus']")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("h3")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='work-experience']/div/div/div[1]/h2")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("work-experience")).perform()


    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("personal-info")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.parallax-content.full-screen")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("p")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("h1")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.cv-section-title")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("p")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.span12")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("div.parallax-content.full-screen")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("2.WORK EXPERIENCE")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("menu")).perform()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("3.TECHNICAL SKILLS")).perform()
    wd.find_element_by_link_text("3.TECHNICAL SKILLS").click()
    wd.implicitly_wait(2)
    ActionChains(wd).move_to_element(wd.find_element_by_id("nav")).perform()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
    else:
        print "Test passed."
