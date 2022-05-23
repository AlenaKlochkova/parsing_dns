from selenium import webdriver
from driver_object import Driver_Object
from constants import *


PROXY_STR = "111.222.111.222:1234"

options = webdriver.FirefoxOptions()
options.add_argument('--proxy-server=%s' % PROXY_STR)

driver = webdriver.Firefox(options=options)
browser = Driver_Object(driver)

browser.go_to(dns)
browser.option(pc_sidebar)
browser.option(detail_pc)

components = [processor, motherboard, videocard, RAM, powerunit, case, cooler, HDD]

for component in components:
    browser.option(component['link'])
    if 'subcategory' in component:
        browser.option(component['subcategory'])
    index = 1
    browser.open_file(component['name'])
    array_of_component = []

    for page in range(1, 11):
        driver.refresh()
        browser.loading(catalog_list)
        item_list = browser.get_list(catalog_list)

        for item in item_list:
            browser.new_tab(item)
            browser.to_new_tab()
            browser.loading(item_price)
            dict_of_item = {
                'model': f'catalog_app.{component["name"]}',
                'pk': index,
                'fields': {
                    'item_model': browser.get_info(component['model']),
                    'detail': browser.get_info(item_description)[:-10],
                    'price': browser.get_info(item_price)[:-2]
                }
            }
            array_of_component.append(dict_of_item)
            index += 1
            browser.previous_tab()
        if page < 10:
            browser.option(next_page)
    browser.write_down(array_of_component)
    browser.close_file()
    browser.option(back_to_main_catalog)

driver.quit()
