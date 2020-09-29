def close_modal(driver):
    close_button = ''
    error = True
    while error:
        try:
            close_button = driver.find_element_by_xpath("//div[@class='ReactModal__Overlay ReactModal__Overlay--after-open']")
            close_button.click()
            print('close_button', close_button)
            if close_stylish_modal:
                error = False
                print('Close modal triggered')
        except:
            if not close_button:
                error = False
                print('No modal')


def close_stylish_modal(driver):
    close_stylish_modal_button = ''
    error = True
    while error:
        try:
            close_stylish_modal_button = driver.find_element_by_xpath("//div[@class='bluecoreOverlay']")
            close_stylish_modal_button.click()
            print('close_stylish_modal_button', close_stylish_modal_button)
            if close_stylish_modal:
                error = False
                print('Close Stylish modal triggered')
        except:
            if not close_stylish_modal_button:
                error = False
                print('No Stylish modal')


def close_stylish_modal2(driver):
    error = True
    while error:
        try:
            close_stylish_modal_button2 = driver.find_element_by_xpath("//div[@class='preScreenElement bluecoreCloseButton']")
            print('close_stylish_modal_button2', close_stylish_modal_button2)
            if close_stylish_modal2:
                error = False
        except:
            print('No Stylish modal2')
            # error = False


def get_page_running_despite(driver):
    error = True
    error_message = ''
    while error:
        try:
            error_message = driver.find_element_by_xpath("//h1[text()='Access Denied']")
            print('error_message', error_message)
            if error_message:
                error_message = ''
                driver.refresh()
                print('Refresh page: get page running despite...')
        except:
            if not error_message:
                error = False
                error_message = ''
                print('Continue get page running despite...')


def get_page_running(driver):
    error = True
    error_message = ''
    while error:
        try:
            error_message = driver.find_element_by_xpath("//h1[text()='429 Too Many Requests']")
            print('error_message', error_message)
            if error_message:
                error_message = ''
                driver.refresh()
                print('Continue get page running despite...')
        except:
            if not error_message:
                error = False
                error_message = ''
                print('Continue get page running...')


def close_all_the_modals(driver):
    close_modal(driver)
    close_stylish_modal(driver)


def get_the_page_running_all_in_all(driver):
    get_page_running(driver)
    get_page_running_despite(driver)
