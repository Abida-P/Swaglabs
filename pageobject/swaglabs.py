from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def username():
    return "//android.widget.EditText[@content-desc='test-Username']"
def password():
    return "//android.widget.EditText[@content-desc='test-Password']"

def login():
    return "//android.widget.TextView[@text='LOGIN']"

def count1():
    return "//android.widget.TextView[@content-desc='test-Item title']"

def cart1():
    return "(//android.view.ViewGroup[@content-desc='test-ADD TO CART'])[1]"
def cart2():
    return "//android.view.ViewGroup[@content-desc='test-ADD TO CART']"
def cart_image():
    return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
def remove():
    return "//android.view.ViewGroup[@content-desc='test-REMOVE']"
def cart_image2():
    return "//android.view.ViewGroup[@content-desc='test-Cart']/android.view.ViewGroup/android.widget.ImageView"
def hover(driver):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(578, 2252)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(550, 1041)
    actions.w3c_actions.pointer_action.release()
    actions.perform()

def checkout():
    return "new UiSelector().text(\"CHECKOUT\")" 
def firstname():
    return "test-First Name"  
def lastname():
    return "test-Last Name"
def postalcode():
    return "test-Zip/Postal Code" 

def con():
    return "new UiSelector().text(\"CONTINUE\")"
def finish():
    return "new UiSelector().text(\"FINISH\")"

