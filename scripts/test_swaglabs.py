
import pytest
from appium import webdriver
import time
from appium.options.common import AppiumOptions
from pageobject import swaglabs
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput





@pytest.mark.usefixtures("launch_app")
class TestSwaglabs:

    
    def test_sauce_labs_login(self,read_json):
        self.driver.find_element(AppiumBy.XPATH,swaglabs.username()).send_keys(read_json["username"])
        time.sleep(2)
        # el1.sendKeys("standard_user")
        self.driver.find_element(AppiumBy.XPATH,swaglabs.password()).send_keys(read_json["password"])
        # el2.sendKeys("secret_sauce")
        self.driver.find_element(AppiumBy.XPATH,swaglabs.login()).click()
        time.sleep(2)    

    def test_add_to_cart(self):
           
        count = len(self.driver.find_elements(AppiumBy.XPATH,swaglabs.count1()))
        for i in range(1,count+1):
            item = self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@content-desc='test-Item title'])["+str(i)+"]").text
            print(item)
 
        self.driver.find_element(AppiumBy.XPATH,swaglabs.cart1()).click()
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH, swaglabs.cart2()).click()
        time.sleep(3)

    def test_validate_cart(self,read_json):
            self.driver.find_element(AppiumBy.XPATH,swaglabs.cart_image()).click()
            time.sleep(2)
            cart_count = len(self.driver.find_elements(AppiumBy.XPATH, swaglabs.remove()))
            print("item in cart is :",cart_count)
 
            self.driver.find_element(AppiumBy.XPATH,swaglabs.cart_image2() ).click()
            time.sleep(2)  

            # actions = ActionChains(self.driver)
            # actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            # actions.w3c_actions.pointer_action.move_to_location(578, 2252)
            # actions.w3c_actions.pointer_action.pointer_down()
            # actions.w3c_actions.pointer_action.move_to_location(550, 1041)
            # actions.w3c_actions.pointer_action.release()
            # actions.perform()
            swaglabs.hover(self.driver)

            el7 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.checkout())
            el7.click()
            time.sleep(2)
            el8 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.firstname())
            el8.send_keys(read_json["First Name"])
            time.sleep(2)
            el9 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.lastname())
            el9.send_keys(read_json["Last Name"])
            time.sleep(2)
            el10 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.postalcode())
            el10.send_keys(read_json["postal code"])
            time.sleep(2)
            el11 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.con())
            el11.click()
            time.sleep(2)
            # actions = ActionChains(self.driver)
            # actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
            # actions.w3c_actions.pointer_action.move_to_location(601, 2257)
            # actions.w3c_actions.pointer_action.pointer_down()
            # actions.w3c_actions.pointer_action.move_to_location(472, 739)
            # actions.w3c_actions.pointer_action.release()
            # actions.perform()
            swaglabs.hover(self.driver)


            el12 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.finish())
            el12.click()
            time.sleep(2)

            



    def close_driver(self):
        self.driver.quit()
        print("Driver instance closed successfully...")
        time.sleep(5)    

