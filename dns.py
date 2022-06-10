from selenium import webdriver
from driver_object import Driver_Object
import os
from constants import *


PROXY_STR = "111.222.111.222:1234"

options = webdriver.FirefoxOptions()
options.add_argument('--proxy-server=%s' % PROXY_STR)

driver = webdriver.Firefox(options=options)
browser = Driver_Object(driver)

browser.go_to(dns)
browser.option(pc_sidebar)

components = [processor, motherboard, videocard, RAM, powerunit, case, cooler, HDD]

for component in components:
    browser.option(component['link'])
    if 'subcategory' in component:
        browser.option(component['subcategory'])
    index = 1
    array_of_component = []
    os.mkdir(component['name'])

    for page in range(1, 11):
        driver.refresh()
        browser.loading(catalog_list)
        item_list = browser.get_list(catalog_list)
        for item in item_list:
            browser.focus(item)
            browser.new_tab(item)
            browser.to_new_tab()
            browser.loading(item_price)
            item_model = browser.get_info(component['model'])
            image_url = browser.image_link(item_image)
            dict_of_item = {
                'model': f'catalog_app.{component["name"]}',
                'pk': index,
                'fields': {
                    'image': f'{component["name"]}/{item_model}.jpg',
                    'model': item_model,
                    'description': browser.get_info(item_description)[:-10],
                    'price': int(browser.get_info(item_price)[:-2].replace(' ', ''))
                }
            }
            browser.save_image(image_url, component, item_model)
            array_of_component.append(dict_of_item)
            index += 1
            browser.previous_tab()
        if page < 10:
            browser.option(next_page)
    browser.open_file(component['name'])
    browser.write_down(array_of_component)
    browser.close_file()
    browser.option(back_to_main_catalog)

driver.quit()
