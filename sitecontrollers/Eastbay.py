from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import threading
# import multiprocessing
# from multiprocessing.dummy import Pool
# from selenium.webdriver.chrome.options import Options
# pool = Pool(10)

from utilities.partial_update_task import partial_update_task
from utility_functions.close_modals_get_page import (close_modal, close_stylish_modal, get_page_running,
                                                    get_page_running_despite, close_all_the_modals,
                                                    get_the_page_running_all_in_all)
from utility_functions.configure_specifications import select_size, add_to_cart, view_cart, check_out, type_quantity
from utility_functions.fill_forms import (fill_mailing_address_form, save_form_and_continue, 
                                        fake_wait, fill_card_details, place_order)
from utility_functions.chrome_options import chrome_options
from utility_functions.proxies import proxies

class Eastbay:
    """docstring for Eastbay."""
  
    def generate_url(self, product_details, user_details, taskId):
        product_name = product_details.get('product_name').lower().replace("'", '').replace(' - ', '-').replace(' ', '-').replace('---', '-').replace('_', '-')

        derived_url = 'https://www.eastbay.com/product/' + product_name + '/' + product_details['product_number'] + '.html'
        product_size = product_details.get('product_size')
        product_quantity = product_details.get('product_quantity')

        product_summary = {
            'url': derived_url, 'size': product_size, 'quantity': product_quantity
        }

        return self.get_product_page(product_summary, user_details, taskId)
        # purchase = pool.apply_async(self.get_product_page, args=(product_summary, user_details))
        # return multiprocessing.cpu_count()

    def get_product_page(self, product_summary, user_details, taskId):
        url = product_summary.get('url')
        size = product_summary.get('size')
        quantity = product_summary.get('quantity')
        state_name = user_details['state']

        # driver = webdriver.Chrome(options=chrome_options)
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        print('Chrome Initialized')
        
        driver.get(url)
        print('Got Url')
        
        wait = WebDriverWait(driver, 40)
        print('Wait Initialized')
        driver.get_screenshot_as_file("screenshots/eastbay/screenshot1.png")

        get_the_page_running_all_in_all(driver)

        close_all_the_modals(driver)
        select_size(driver, size, 'Size Selected')

        close_all_the_modals(driver)
        type_quantity(driver, 'Quntity Typed', quantity)

        close_all_the_modals(driver)
        add_to_cart(driver, 'Added to Cart')
        driver.get_screenshot_as_file("screenshots/eastbay/screenshot2.png")

        get_the_page_running_all_in_all(driver)

        close_all_the_modals(driver)
        view_cart(driver, 'Cart Viewed')

        close_all_the_modals(driver)
        check_out(driver, 'Checked Out')
        driver.get_screenshot_as_file("screenshots/eastbay/screenshot3.png")

        fill_mailing_address_form(driver, wait, user_details, state_name, 'Address Details Provided')
        
        close_all_the_modals(driver)
        save_form_and_continue(driver, 'Save and Continue Clicked')
        driver.get_screenshot_as_file("screenshots/eastbay/screenshot4.png")

        close_all_the_modals(driver)
        fake_wait(wait)
        
        driver.switch_to.default_content()
        all_frames = driver.find_elements_by_tag_name('iframe')

        fill_card_details(driver, 'encryptedCardNumber', user_details['card_number'], all_frames)
        fill_card_details(driver, 'encryptedExpiryMonth', user_details['card_expiry'].split(' / ', 1)[0], all_frames)
        fill_card_details(driver, 'encryptedExpiryYear', user_details['card_expiry'].split(' / ', 1)[1], all_frames)
        fill_card_details(driver, 'encryptedSecurityCode', user_details['card_cvv'], all_frames)

        place_order(wait, 'Place Order Clicked')

        partial_update_task(taskId, 'Ordered')
        driver.get_screenshot_as_file("screenshots/eastbay/screenshot5.png")
        driver.quit()
        return {'success': True, 'message': 'Ordered'}
