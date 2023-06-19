import logging
import allure
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
import time


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Checking if element in currently visible in view")
    def check_element_in_view(self, locator):
        time.sleep(2) #wait for page to scroll to element
        result = self.browser.execute_script(f'let el = document.querySelector("{locator[1]}"); let rect = '
                                           f'el.getBoundingClientRect();return (rect.top >= 0 && rect.left >= 0 && '
                                           f'rect.bottom <= (window.innerHeight || '
                                           f'document.documentElement.clientHeight) && rect.right <= ('
                                           f'window.innerWidth || document.documentElement.clientWidth));')
        if not result:
            self.logger.warning(f"Element with locator {locator} isn't in view")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element with locator {locator} isn't in view")
        return result


    def open(self, relative_url=""):
        with allure.step(f"Opening {self.url}{relative_url} url"):
            self.logger.info(f"Opening {self.url}{relative_url} url")
            self.browser.get(self.url + relative_url)

    @allure.step("Saving current url")
    def get_current_url(self):
        self.logger.info("Getting current url")
        return self.browser.current_url

    @allure.step("Checking if the {_selector} element is present on page")
    def is_element_present(self, _by, _selector):
        self.logger.info(f"Trying to find '{_selector}' element by '{_by}'")
        try:
            self.browser.find_element(_by, _selector)
        except NoSuchElementException:
            self.logger.warning(f"Couldn't find element")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            return False
        return True

    @allure.step("Waiting for the {_selector} element for {timeout} seconds")
    def wait_for_element(self, _by, _selector, timeout=2):
        self.logger.info(f"Waiting for {_selector} element by {_by} for {timeout} seconds")
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((_by, _selector)))
        except TimeoutException:
            self.logger.warning(f"Element wasn't found in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Couldn't find element for {timeout} seconds")
        return element

    @allure.step("Waiting for all the {_selector} elements for {timeout} seconds")
    def wait_for_elements(self, _by, _selector, timeout=2):
        self.logger.info(f"Waiting for all the {_selector} elements by {_by} for {timeout} seconds")
        try:
            elements = WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located((_by, _selector)))
        except TimeoutException:
            self.logger.warning(f"Elements weren't found in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Couldn't find elements for {timeout} seconds")
        return elements

    @allure.step("Waiting for '{_selector}' element to appear and then clicking on it when it becomes clickable")
    def wait_for_element_and_click(self, _by, _selector, timeout=2):
        element = self.wait_for_element(_by, _selector, timeout)
        self.logger.info(f"clicking '{element}' element")
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable((_by, _selector))).click()
        except ElementNotInteractableException:
            self.logger.warning(f"Cannot click on element {element}")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Cannot click on element {element}")



    @allure.step("Waiting for '{_selector}' element to disappear for {timeout} seconds")
    def wait_for_element_to_disappear(self, _by, _selector, timeout=2):
        self.logger.info(f"Waiting for {_selector} element by {_by} for {timeout} seconds to disappear")
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((_by, _selector)))
        except TimeoutException:
            self.logger.warning(f"Element didn't disappear in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element didn't disappear in {timeout} seconds")

    @allure.step("Waiting for '{element}' element to be stale")
    def wait_for_element_to_stale(self, element, timeout=2):
        self.logger.info(f"Waiting for '{element}' element to be stale")
        try:
            WebDriverWait(self.browser, timeout).until(EC.staleness_of(element))
        except TimeoutException:
            self.logger.warning(f"Element didn't stale in {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element didn't stale in {timeout} seconds")

    @allure.step("Waiting for element with selector '{_selector} to be invisible'")
    def wait_for_element_to_be_invisible(self, _by, _selector, timeout=2):
        self.logger.info(f"Waiting for element with selector'{_selector} to be invisible'")
        try:
            WebDriverWait(self.browser, timeout).until_not(EC.visibility_of_element_located((_by, _selector)))
        except TimeoutException:
            self.logger.warning(f"Element with selector {_selector} is still visible after {timeout} seconds")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Element  with selector {_selector} was still visible after {timeout} seconds")

    @allure.step("Sending data = '{data}' into '{_locator}' element")
    def enter_data(self, _by, _locator, data):
        element = self.wait_for_element(_by, _locator)
        element.clear()
        self.logger.info(f"Sending data = '{data}' into '{_locator}' element")
        element.send_keys(data)

    @allure.step("Logging in by adding auth cookie")
    def add_auth_cookie(self, auth_cookie):
        self.browser.get('https://planyway.com')
        self.browser.add_cookie(auth_cookie[0])

    @allure.step("Picking random element from list")
    def pick_random_element(self, locator, timeout=2):
        self.logger.info(f"Finding all available elements for {locator}")
        list_of_elements = self.wait_for_elements(*locator, timeout)
        try:
            WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except ElementNotInteractableException:
            self.logger.warning(f"Cannot click on element {locator}")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Cannot click on element {locator}")

        amount_of_elements = len(list_of_elements) - 1
        if amount_of_elements < 0:
            raise AssertionError(f"No available elements were found with {locator} ")
        else:
            return list_of_elements[random.randint(0, amount_of_elements)]

    '''
    Custom wait to check if URL has changed to expected one
    '''
    def url_changed(self, expected_url):
        def __predicate(driver):
            self.logger.info(f'current url = {driver.current_url}, expected url = {expected_url}')
            if driver.current_url == expected_url:
                return True
            return False
        return __predicate

    @allure.step("Check if url has changed")
    def wait_for_ulr_change(self, expected_url, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(self.url_changed(expected_url))
        except TimeoutException:
            self.logger.warning(f"URL has not changed to expected in {timeout} seconds or changed to unexpected url")
            allure.attach(
                name=self.browser.session_id,
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"URL has not changed to expected in {timeout} seconds or changed to unexpected url")