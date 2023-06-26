import pytest
import logging


from selenium import webdriver


logging.basicConfig(level=logging.INFO, filename="logs/selenium.log", filemode="w")
browser_logger = logging.getLogger("BROWSER_LOGGER")


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     choices=["chrome", "firefox"],
                     default="chrome")
    parser.addoption("--url",
                     action="store",
                     default="rubius.com")
    parser.addoption("--executor",
                     action="store",
                     default="local")
    parser.addoption("--bversion",
                     action="store")
    parser.addoption("--vnc",
                     action="store_true",
                     default=False)
    parser.addoption("--video",
                     action="store_true",
                     default=False)
    parser.addoption("--logs",
                     action="store_true",
                     default=False)
    parser.addoption("--headless",
                     action="store_true",
                     default=False)


@pytest.fixture
def browser(request):
    test_name = request.node.name

    def teardown():
        browser_logger.info("==============> CLOSING DRIVER")
        driver.quit()

    driver = None
    browser_choice = request.config.getoption("--browser")
    executor_choice = request.config.getoption("--executor")
    browser_version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    video = request.config.getoption("--video")
    logs = request.config.getoption("--logs")
    headless = request.config.getoption("--headless")

    if executor_choice == "local":

        if browser_choice == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
        elif browser_choice == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless=new")
            driver = webdriver.Firefox(options=options)
    else:
        executor_url = f"http://{executor_choice}:4444/wd/hub"
        caps = {
            "browserName": browser_choice,
            "browserVersion": browser_version,
            "selenoid:options": {
                "name": test_name,
                "enableVNC": vnc,
                "enableVideo": video,
                "enableLog": logs
            }
        }
        if browser_choice == "chrome":
            options = webdriver.ChromeOptions()
        else:
            options = webdriver.FirefoxOptions()
        for cap in caps.items():
           options.set_capability(cap[0], cap[1])
        driver = webdriver.Remote(
            command_executor=executor_url,
            options=options)

    request.addfinalizer(teardown)
    driver.set_window_size(1960, 1080)
    browser_logger.info(f"==============> Starting {test_name}")
    return driver



@pytest.fixture
def url(request):
    return f'https://{request.config.getoption("--url")}'
