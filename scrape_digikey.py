from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


# TODO: scrape many pages at the same time.
# TODO: use docker containers with driver and delete driver
def find_part_infos(url):
    driver = webdriver.Chrome()
    driver.get(url)

    delay = 3

    try:
        WebDriverWait(driver, delay).until(ec.presence_of_element_located((By.ID, 'header')))
        print("Page is ready")
    except TimeoutException:
        print("Loading took too much time")

    name = driver.find_element_by_tag_name("h1").text
    unit = driver.find_element_by_xpath(("//table[@class='product-dollars']/tbody/tr[2]/td")).text
    price = driver.find_element_by_xpath(("//table[@class='product-dollars']/tbody/tr[2]/td[3]")).text
    description = driver.find_element_by_xpath("//td[@itemprop='description']").text
    digikey_part_number = driver.find_element_by_id("reportPartNumber").text

    driver.close()

    part_info = {'name': name, 'unit': unit, 'price': price,
                 'description': description, 'digikey_part_number': digikey_part_number, 'url': url}

    return part_info
