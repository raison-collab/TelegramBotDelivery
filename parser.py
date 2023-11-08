import json
from time import sleep

from loguru import logger
from selenium.webdriver import Chrome

from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def __wait_such_element(
        driver: WebDriver,
        by: By, value: str,
        interval: int = 1,
        limit: int = -1
) -> WebElement | None:
    attempt = 0
    while True:
        try:
            if attempt == limit:
                return None
            attempt += 1
            return driver.find_element(by, value)
        except NoSuchElementException:
            sleep(interval)


def parse_yandex_lavka(url: str, cookie_path: str) -> dict:
    options = Options()
    options.add_argument('headless')

    driver = Chrome(options=options)
    driver.get(url)

    with open(cookie_path, encoding="utf-8", mode="r") as file:
        cookies = json.loads(file.read())
        for cookie in cookies:
            driver.add_cookie(cookie)
            logger.debug(f'Куки {cookie} добавлены')

    driver.refresh()

    info = __wait_such_element(
        driver,
        By.CSS_SELECTOR,
        "#root > div.hjhf26i > header > div:nth-child(6) > button"
    )
    info.click()

    tab = __wait_such_element(driver, By.CLASS_NAME, 'cnw6bwb')

    li_tags = tab.find_elements(By.TAG_NAME, 'li')

    data = {}

    for li_tag in li_tags:
        span_tags = li_tag.find_elements(By.TAG_NAME, 'span')
        data[span_tags[0].text.replace('\u202f', '')] = span_tags[1].text.replace('\u202f', '')

    return data
