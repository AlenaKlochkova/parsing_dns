from selenium.webdriver.common.by import By


dns = 'https://www.dns-shop.ru/'
search_bar = (By.CSS_SELECTOR, 'div.ui-input-search:nth-child(1) > input:nth-child(1)')
pc_sidebar = (By.CSS_SELECTOR, 'div.menu-desktop__root:nth-child(4) > div:nth-child(2) > a:nth-child(1)')
detail_pc = (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(3)')
last_page_attribute = 'data-page-number'
total_pages = (By.CSS_SELECTOR, 'ul.pagination-widget__pages li:last-child')
next_page = (By.CSS_SELECTOR, 'a.pagination-widget__page-link.pagination-widget__page-link_next')
catalog_list = (By.CSS_SELECTOR, 'a.catalog-product__name.ui-link')
back_to_main_catalog = (By.CSS_SELECTOR, 'li.breadcrumb-list__item:nth-child(3) > a:nth-child(1)')
expand_character = (By.CSS_SELECTOR, 'button.product-characteristics__expand')
item_price = (By.CSS_SELECTOR, 'div.product-buy__price')
item_description = (By.CSS_SELECTOR, 'div.product-card-top__specs')
item_image = (By.CSS_SELECTOR, 'picture.product-images-slider__main source')

processor = {
    'link': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(2)'),
    'name': 'processor',
    'model': (By.CSS_SELECTOR, 'div.product-characteristics div.product-characteristics__group:nth-child(2) div.product-characteristics__spec div.product-characteristics__spec-value')
}

motherboard = {
    'link': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(3)'),
    'name': 'motherboard',
    'model': (By.CSS_SELECTOR, 'div.product-characteristics div.product-characteristics__group:nth-child(2) div.product-characteristics__spec:nth-child(3) div.product-characteristics__spec-value')
}

videocard = {
    'link': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(4)'),
    'name': 'videocard',
    'model': (By.CSS_SELECTOR, 'div.product-characteristics div.product-characteristics__group:nth-child(2) div.product-characteristics__spec:nth-child(3) div.product-characteristics__spec-value')
}

RAM = {
    'subcategory': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(2)'),
    'link': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(5)'),
    'name': 'RAM',
    'model': (By.CSS_SELECTOR, 'div.product-characteristics div.product-characteristics__group:nth-child(2) div.product-characteristics__spec:nth-child(3) div.product-characteristics__spec-value')
}

powerunit = {
    'link': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(6)'),
    'name': 'powerunit',
    'model': (By.CSS_SELECTOR, 'div.product-characteristics div.product-characteristics__group:nth-child(2) div.product-characteristics__spec:nth-child(3) div.product-characteristics__spec-value')
}

case = {
    'link': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(7)'),
    'name': 'case',
    'model': (By.CSS_SELECTOR, 'div.product-characteristics div.product-characteristics__group:nth-child(2) div.product-characteristics__spec:nth-child(3) div.product-characteristics__spec-value')
}

cooler = {
    'subcategory': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(2)'),
    'link': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(8)'),
    'name': 'cooler',
    'model': (By.CSS_SELECTOR, 'div.product-characteristics div.product-characteristics__group:nth-child(2) div.product-characteristics__spec:nth-child(3) div.product-characteristics__spec-value')
}

HDD = {
    'subcategory': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(2)'),
    'link': (By.CSS_SELECTOR, 'a.subcategory__item:nth-child(11)'),
    'name': 'hdd',
    'model': (By.CSS_SELECTOR, 'div.product-characteristics div.product-characteristics__group:nth-child(2) div.product-characteristics__spec:nth-child(3) div.product-characteristics__spec-value')
}









