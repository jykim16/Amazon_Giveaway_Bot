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


class AmazonBot():
    def __init__(self, email, password, link=AMAZON_GIVEAWAY_LINK):
        opts = Options()
        # comment out below if you want to see the browser UI 
        #opts.set_headless()
        self.browser = Chrome(options=opts)
        self.actions = ActionChains(self.browser)
        self.email = email
        self.password = password

        # site for amazon giveaway
        self.browser.get(AMAZON_GIVEAWAY_LINK)
        print("run bot.prime_giveaway()")    

    def prime_giveaway(self):
        self.login()
        self.select_giveaways()

    def login(self):
        self.actions = ActionChains(self.browser)
        self.browser.find_elements_by_id('nav-link-accountList')[0].click()
        self.actions.send_keys(self.email).perform()
        self.browser.find_element_by_id('continue').click() 
        self.browser.find_element_by_id('ap_password').send_keys(self.password) 
        self.browser.find_element_by_id('signInSubmit').click() 

    def select_giveaways(self):
        # get all giveaway items
        items = self.browser.find_elements_by_class_name('bxc-grid-overlay__link')

        # create tabs for each giveaway item
        actions = self.actions.key_down(Keys.COMMAND)
        for item in items:
            actions = actions.click(item)

        actions = actions.key_up(Keys.COMMAND)
        actions.perform()

        # get all tab handles
        windows = self.browser.window_handles

        # play videos in all windows
        for window in windows:
            self.browser.switch_to.window(window)
            try:
                WebDriverWait(self.browser, 1).until(lambda x: x.find_elements_by_class_name('airy-play-toggle-hint'))
                self.browser.find_elements_by_class_name('airy-play-toggle-hint')[0].click()
            except:
                print('this page doesn\'t have a video')
                self.browser.close()

        # wait 32 seconds
        time.sleep(32)

        #get new windows
        windows = self.browser.window_handles

        # click on submit giveaway bid 
        for window in windows:
            self.browser.switch_to.window(window)
            try:
                self.browser.find_element_by_id('videoSubmitForm').click()
                time.sleep(3)
                # delete this tab
                # self.browser.close()
            except:
                print('no bid found here')

