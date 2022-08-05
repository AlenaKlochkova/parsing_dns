from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import last_page_attribute
import json
from urllib.request import urlretrieve


class Driver_Object():

    def __init__(self, driver):
        self.driver = driver

    """Переходит по указанной ссылке"""

    def go_to(self, link):

        self.driver.get(link)

    def loading(self, selector):

        """Ожидание загрузки страницы"""

        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.visibility_of_element_located(selector))

    def to_new_tab(self):

        """Переход на новую вкладку"""

        self.driver.switch_to.window(self.driver.window_handles[-1])

    def previous_tab(self):

        """Закрывает последнюю открытую вкладку, переходит на предыдущую вкладку"""

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def option(self, selector):

        """Ищет элемент и кликает по нему"""

        self.loading(selector)
        self.driver.find_element(*selector).click()

    def open_file(self, file_name):

        """Открывает файл формата json для записи"""

        global file
        file = open(f'{file_name}.json', 'a', encoding='utf-8')

    def write_down(self, source):

        """Записывает указанные данные в открытый файл"""

        json.dump(source, file, indent=4, ensure_ascii=False)

    def close_file(self):

        """Закрывает открытый на данный момент файл"""

        file.close()

    def page_navigation(self, selector):

        """Ищет количество доступных страниц"""
        try:
            self.loading(selector)
            last_page = self.driver.find_element(*selector)
            last_page_number = last_page.get_attribute(last_page_attribute)
            return int(last_page_number)
        except:
            return 2

    def get_info(self, selector):

        """Возвращает текст указанного элемента"""

        return self.driver.find_element(*selector).text

    def new_tab(self, item):

        """Открывает ссылку, указанную в элементе, в новой вкладке"""

        self.driver.execute_script("window.open('" + item.get_attribute('href') + "', 'new window')")

    def get_list(self, selector):

        """Возвращает список элементов с указанным селектором"""

        return self.driver.find_elements(*selector)

    def image_link(self, selector):

        """Возвращает ссылку, указанную в атрибуте элемента"""

        return self.driver.find_element(*selector).get_attribute('srcset')

    def focus(self, item):

        """Пролистывает страницу до указанного элемента"""

        self.driver.execute_script("arguments[0].scrollIntoView();", item)

    def save_image(self, link, component, item_model):

        """Сохраняет картинку по ссылке в указанную директорию"""

        urlretrieve(link, f'{component["name"]}/{item_model}.jpg')

    def get_price(self, item_price):
        price = self.get_info(item_price)
        end_price = price.find('₽')
        price = price[:end_price].replace(' ', '')
        return int(price)

    def to_next_page(self, selector):
        self.loading(selector)
        next_page = self.driver.find_element(*selector)
        self.driver.execute_script("arguments[0].click();", next_page)
