from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from PIL import Image
from io import BytesIO

driver = None
try:
    driver = webdriver.Chrome('/Users/junho85/Downloads/chromedriver')
    driver.get("https://github.com/junho85")

    elem = driver.find_element_by_class_name("js-yearly-contributions")
    last_date_elem = elem.find_element_by_tag_name("svg").find_elements_by_tag_name("rect")[-1]
    location = last_date_elem.location

    driver.set_window_size(1200, 500)
    driver.execute_script("window.scrollBy(0, 800);")
    ActionChains(driver).move_to_element(last_date_elem).perform()

    png = driver.get_screenshot_as_png()
    img = Image.open(BytesIO(png))

    img.crop((1900, 150, 2300, 550)).save("screenshot.png")
finally:
    driver.close()
