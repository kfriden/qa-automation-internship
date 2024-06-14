from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


# Run Behave Tests with Allure results
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/off_plan_products.feature


def browser_init(context):
    """
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    # FIREFOX BROWSER
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # HEADLESS MODE
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('--window-size=1920,1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(options = options, service = service)

    # BROWSERSTACK CODE #
    # bs_user = 'kaitlynfriden_y2mXKl'
    # bs_key = 'eQHRTGhV6JqHDHTJNyFm'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'OS X',
    #     'osVersion': 'Monterey',
    #     'browserName': 'Edge',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # MOBILE EMULATION
    # For Custom screen Pixel size in mobile testing
    mobile_emulation = {
        "deviceMetrics": {
            "width": 390,  # Replace with your custom width
            "height": 844,  # Replace with your custom height
            "pixelRatio": 3  # Replace with your custom pixel ratio
        },
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Mobile/15E148 Safari/604.1"
    }
    # With Device name Testing of Mobile on Web
    # mobile_emulation = {
    #     "deviceName": "iPhone SE"  # You can use other device names as well
    # }
    # Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)
    context.driver.execute_script("document.body.style.zoom='50%'")

    context.driver.maximize_window()

    context.driver.maximize_window()
    context.driver.implicitly_wait(6)
    context.driver.wait = WebDriverWait(context.driver, timeout=15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)
    # browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        context.app.base_page.save_screenshot(step)


def after_scenario(context):
    context.driver.delete_all_cookies()
    context.driver.quit()
