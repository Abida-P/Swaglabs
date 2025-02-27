import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from appium import webdriver

@pytest.fixture(scope="class")
def launch_app(request):
    try:
        cap= {
            "appium:deviceNmae": "Samsung",
            "appium:platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:app": "C:\\Users\\2022369\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk",
            "appium:appWaitActivity": "com.swaglabsmobileapp.MainActivity"
        }

        print("initiating App instance driver")
        driver=webdriver.Remote("http://localhost:4723/wd/hub",options=AppiumOptions().load_capabilities(cap))
        request.cls.driver=driver

        yield driver
        driver.quit()
    except:
        print("unable to launch  the appp")

@pytest.fixture
def read_json():
    with open("C:\\quest_topics\\testdata\\input.json") as config_file:
        data = json.load(config_file)
    return data    

