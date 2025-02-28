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
        try:
            self.driver.find_element(AppiumBy.XPATH,swaglabs.username()).send_keys(read_json["username"])
            time.sleep(2)
            # el1.sendKeys("standard_user")
            self.driver.find_element(AppiumBy.XPATH,swaglabs.password()).send_keys(read_json["password"])
            # el2.sendKeys("secret_sauce")
            self.driver.find_element(AppiumBy.XPATH,swaglabs.login()).click()
            time.sleep(2)  
            el6 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.grid())
            el6.click()
            time.sleep(2)
            el7 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.filter_option())
            el7.click()
            time.sleep(2)
            el8 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.low_to_high())
            el8.click()
            time.sleep(2)

            item1 = self.driver.find_element(AppiumBy.XPATH, swaglabs.low_h1()).text
            price_item1 = ''.join(char for char in item1 if char.isdigit())

            item2 = self.driver.find_element(AppiumBy.XPATH, swaglabs.low_h2()).text
        
            price_item2 = ''.join(char for char in item2 if char.isdigit())

            if int(price_item1) < int(price_item2):
                print("price of item 1 < price of item 2")

                el9 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.filter_option())
                el9.click()
                time.sleep(2)
                el10 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.high_to_low())
                el10.click()
                time.sleep(2)
    
                item3 = self.driver.find_element(AppiumBy.XPATH, swaglabs.high_l1()).text
            
                price_item3 = ''.join(char for char in item3 if char.isdigit())
    
                item4 = self.driver.find_element(AppiumBy.XPATH, swaglabs.high_l2()).text
            
                price_item4 = ''.join(char for char in item4 if char.isdigit())
    
                if int(price_item3) > int(price_item4):
                    print("price of item 1 > price of item 2")
    
                pdt_count = len(self.driver.find_elements(AppiumBy.XPATH, swaglabs.pdt_count()))
                for i in range(1,pdt_count+1):
                    name = self.driver.find_element(AppiumBy.XPATH, swaglabs.pdt_name(i)).text
                    print(name)
    
                el11 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.list_prod1())
                el11.click()
                time.sleep(2)
                el13 = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=swaglabs.list_prod2())
                el13.click()
                time.sleep(2)
                self.driver.find_element(AppiumBy.XPATH, swaglabs.cart()).click()
                time.sleep(2)
                time.sleep(2)
    
                swaglabs.scroll(self.driver)
    
                el9 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.checkout())
                el9.click()
                time.sleep(2)
    
                el10 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.first_name())
                el10.send_keys(read_json["First Name"])
                time.sleep(2)
    
                el11 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.last_name())
                el11.send_keys(read_json["Last Name"])
                time.sleep(2)
    
                el12 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.pin())
                el12.send_keys(read_json["postal code"])
                time.sleep(2)
    
                el13 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.continue_button())
                el13.click()
                time.sleep(2)
            
                swaglabs.scroll(self.driver)
    
                el14 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=swaglabs.finish())
                el14.click()
                time.sleep(2)
 
        except:
            print("Failed")
 
    def test_close_driver(self):
        self.driver.quit()
        print("Driver Instance Closed Successfully...")
        time.sleep(20)

    
        # count = len(self.driver.find_elements(AppiumBy.XPATH, swaglabs.itemCount()))
        # for i in range(1,count+1):
        #     item = self.driver.find_element(AppiumBy.XPATH,swaglabs.printItem(i)).text
        #     print(item)
       


