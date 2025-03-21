# from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
# from appium.options.common import AppiumOptions
# from appium.webdriver.appium_service import AppiumService
# import time
# import pytest
 
# # For W3C actions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
 

# def username():
#     return "//android.widget.EditText[@content-desc='test-Username']"
# def password():
#     return "//android.widget.EditText[@content-desc='test-Password']"

# def login():
#     return "//android.widget.TextView[@text='LOGIN']"

# def count1():
#     return "//android.widget.TextView[@content-desc='test-Item title']"

# def cart1():
#     return "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]"
# def cart2():
#     return "//android.view.ViewGroup[@content-desc='test-ADD TO CART']"
# def cart_image():
#     return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
# def remove():
#     return "//android.view.ViewGroup[@content-desc='test-REMOVE']"
# def cart_image2():
#     return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
# def grid():
#     return "new UiSelector().className(\"android.widget.ImageView\").instance(4)"
 
# def filter_option():
#     return "new UiSelector().className(\"android.widget.ImageView\").instance(5)"
# def low_to_high():
#     return "new UiSelector().text(\"Price (low to high)\")"
 
# def low_h1():
#     return "//android.widget.TextView[@content-desc='test-Price' and @text='$7.99']"
 
# def low_h2():
#     return "//android.widget.TextView[@content-desc='test-Price' and @text='$9.99']"
# def high_to_low():
#     return "new UiSelector().text(\"Price (high to low)\")"
 
# def high_l1():
#     return "//android.widget.TextView[@content-desc='test-Price' and @text='$49.99']"
 
# def high_l2():
#     return "//android.widget.TextView[@content-desc='test-Price' and @text='$29.99']"
 
# def list_prod1():
#     return "new UiSelector().text(\"+\").instance(1)"
 
# def list_prod2():
#     return "new UiSelector().text(\"+\").instance(2)"
 
# # def hover(driver):
# #     actions = ActionChains(driver)
# #     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
# #     actions.w3c_actions.pointer_action.move_to_location(578, 2252)
# #     actions.w3c_actions.pointer_action.pointer_down()
# #     actions.w3c_actions.pointer_action.move_to_location(550, 1041)
# #     actions.w3c_actions.pointer_action.release()
# #     actions.perform()
# def scroll(driver):
#     # global driver
#     actions = ActionChains(driver)
#     actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
#     actions.w3c_actions.pointer_action.move_to_location(571, 1982)
#     actions.w3c_actions.pointer_action.pointer_down()
#     actions.w3c_actions.pointer_action.move_to_location(571, 629)
#     actions.w3c_actions.pointer_action.release()
#     actions.perform()
#     time.sleep(2)

# def checkout():
#     return "new UiSelector().text(\"CHECKOUT\")" 
# def firstname():
#     return "test-First Name"  
# def lastname():
#     return "test-Last Name"
# def postalcode():
#     return "test-Zip/Postal Code" 

# def con():
#     return "new UiSelector().text(\"CONTINUE\")"
# def finish():
#     return "new UiSelector().text(\"FINISH\")"
# def itemCount():
#         return "//android.widget.TextView[@content-desc='test-Item title']"
# def printItem(i):
#         return "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]"
# def cart():
#     return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
 
# def remove():
#     return "//android.view.ViewGroup[@content-desc='test-REMOVE']"
 
# def checkout():
#     return "test-CHECKOUT"
 
# def first_name():
#     return "test-First Name"
 
# def last_name():
#     return "test-Last Name"
 
# def pin():
#     return "test-Zip/Postal Code"
 
# def continue_button():
#     return "test-CONTINUE"
 
# def finish():
#     return "test-FINISH"

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
import time
import pytest
 
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
 
 
 
def scroll(driver):
    # global driver
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(571, 1982)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(571, 629)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(2)
 
def username():
    return "//android.widget.EditText[@content-desc='test-Username']"
 
def password():
    return "//android.widget.EditText[@content-desc='test-Password']"
 
def login():
    return '//android.widget.TextView[@text="LOGIN"]'
 
def pdt_count():
    return "//android.widget.TextView[@content-desc='test-Item title']"
 
def pdt_name(i):
    return "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]"
 
def pdt1():
    return "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]"
 
def pdt2():
    return  "//android.view.ViewGroup[@content-desc='test-ADD TO CART']"
 
def cart():
    return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
 
def remove():
    return "//android.view.ViewGroup[@content-desc='test-REMOVE']"
 
def checkout():
    return "test-CHECKOUT"
 
def first_name():
    return "test-First Name"
 
def last_name():
    return "test-Last Name"
 
def pin():
    return "test-Zip/Postal Code"
 
def continue_button():
    return "test-CONTINUE"
 
def finish():
    return "test-FINISH"
 
def grid():
    return "new UiSelector().className(\"android.widget.ImageView\").instance(4)"
 
def filter_option():
    return "new UiSelector().className(\"android.widget.ImageView\").instance(5)"
 
def low_to_high():
    return "new UiSelector().text(\"Price (low to high)\")"
 
def low_h1():
    return "//android.widget.TextView[@content-desc='test-Price' and @text='$7.99']"
 
def low_h2():
    return "//android.widget.TextView[@content-desc='test-Price' and @text='$9.99']"
 
def high_to_low():
    return "new UiSelector().text(\"Price (high to low)\")"
 
def high_l1():
    return "//android.widget.TextView[@content-desc='test-Price' and @text='$49.99']"
 
def high_l2():
    return "//android.widget.TextView[@content-desc='test-Price' and @text='$29.99']"
 
def list_prod1():
    return "new UiSelector().text(\"+\").instance(1)"
 
def list_prod2():
    return "new UiSelector().text(\"+\").instance(2)"