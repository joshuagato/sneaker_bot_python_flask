from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# def select_size(wait, size, print_message):
def select_size(driver, size, print_message):
    # size = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-form-field c-form-field--radio ProductSize']/label/span[text()='{}']".format(size))))
    counter = 1
    shoesize = ''
    not_seen = True
    while not_seen:
        counter += 1
        if counter == 1000:
            break
        try:
            print('Size', size, str(size))
            # size = driver.find_element_by_xpath("//div[@class='c-form-field c-form-field--radio ProductSize']/label/span[text()='{}']".format(size))
            shoesize = driver.find_element_by_xpath("//div/label/span[text()='{}']".format(str(size)))
            shoesize.click()
            print(print_message)
            not_seen = False
        except:
            if not shoesize:
                not_seen = True
                print('Size button not found yet.')


# def add_to_cart(wait, print_message):
def add_to_cart(driver, print_message):
        # addtocart = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@class='Button ProductDetails-form__action']")))
        counter = 1
        addtocart = ''
        not_seen = True
        while not_seen:
            counter += 1
            if counter == 1000:
                break
            try:
                addtocart = driver.find_element_by_xpath("//button[@class='Button ProductDetails-form__action']")
                addtocart.click()
                print(print_message)
                not_seen = False
            except:
                if not addtocart:
                    not_seen = True
                    print('Add-to-cart button not found yet.')


# def view_cart(wait, print_message):
def view_cart(driver, print_message):
    # view_cart = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='c-cart-added__cta']")))
    counter = 1
    viewcart = ''
    not_seen = True
    while not_seen:
        counter += 1
        if counter == 1000:
            break
        try:
            viewcart = driver.find_element_by_xpath("//div[@class='c-cart-added__cta']")
            viewcart.click()
            print(print_message)
            not_seen = False
        except:
            if not viewcart:
                not_seen = True
                print('View-cart button not found yet.')


# def check_out(wait, print_message):
def check_out(driver, print_message):
    # checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//div/a[text()='Guest Checkout']")))
    counter = 1
    checkout = ''
    not_seen = True
    while not_seen:
        counter += 1
        if counter == 1000:
            break
        try:
            checkout = driver.find_element_by_xpath("//div/a[text()='Guest Checkout']")
            checkout.click()
            print(print_message)
            not_seen = False
        except:
            if not checkout:
                not_seen = True
                print('Checkout button not found yet.')


def type_quantity(driver, print_message, quantity):
    qty = driver.find_element_by_id('tel_quantity')
    qty.send_keys(Keys.BACKSPACE * 5)
    qty.send_keys(Keys.DELETE * 5)
    qty.send_keys(quantity)
    print(print_message)