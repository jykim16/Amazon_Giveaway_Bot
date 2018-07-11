# may need to provide 2 factor auth first time signing on with chrome. 
EMAIL = 'jykim16@gmail.com'
PASSWORD = ''
AMAZON_GIVEAWAY_LINK = 'https://www.amazon.com/b?ie=UTF8&node=16040174011'


# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# driver = webdriver.Remote(
#   command_executor='http://127.0.0.1:4444/wd/hub',
#   desired_capabilities=DesiredCapabilities.CHROME)
# import pudb;pubd.set_trace()
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

opts = Options()
# comment out below if you want to see the browser UI 
opts.set_headless()
browser = Chrome(options=opts)

# site for amazon giveaway
browser.get(AMAZON_GIVEAWAY_LINK)

# login
actions = ActionChains(browser)
browser.find_elements_by_id('nav-link-accountList')[0].click()
actions.send_keys(EMAIL).perform()
browser.find_element_by_id('continue').click()
browser.find_element_by_id('ap_password').send_keys(PASSWORD)
browser.find_element_by_id('signInSubmit').click()

# get all giveaway items
items = browser.find_elements_by_class_name('bxc-grid-overlay__link')

# create tabs for each giveaway item
actions = actions.key_down(Keys.COMMAND)
for item in items:
    actions = actions.click(item)

actions = actions.key_up(Keys.COMMAND)
actions.perform()

# get all tab handles
windows = browser.window_handles

# play videos in all windows
for window in windows:
    browser.switch_to.window(window)
    try:
        WebDriverWait(browser, 1).until(lambda x: x.find_elements_by_class_name('airy-play-toggle-hint'))
        browser.find_elements_by_class_name('airy-play-toggle-hint')[0].click()
    except:
        print('this page doesn\'t have a video')
        browser.close()

# wait 32 seconds
time.sleep(32)

#get new windows
windows = browser.window_handles

# click on submit giveaway bid 
for window in windows:
    browser.switch_to.window(window)
    try:
        browser.find_element_by_id('videoSubmitForm').click()
        time.sleep(3)
        # delete this tab
        # browser.close()
    except:
        print('no bid found here')

