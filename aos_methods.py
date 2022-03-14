import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import datetime
import aos_locators as locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
from selenium.webdriver.chrome.options import Options

# s = Service(executable_path='C:\Capstone Project\chromedriver.exe')
# driver = webdriver.Chrome(service=s)


options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

def setUp():
    print(f'This AOS Test Start at : {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
          f' on {datetime.datetime.today().strftime("%A")}')
    print('-----------------~~~~~~-------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.web_url)
    assert driver.current_url == locators.web_url
    assert driver.title == locators.web_title
    print('Advantage Online Shopping Launched Successfully!!')
    print('')
    sleep(1)


def create_new_user():
    print('-----------------------------Create New User----------------------------------')
    sleep(4)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(1)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.25)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
    sleep(0.25)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(0.25)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(0.25)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(0.25)
    if locators.country == 'Canada':
        pr_list = ['BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NB', 'PB', 'NL', 'NS']
        for li in pr_list:
            locators.rand_province = random.choice(pr_list)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.rand_province)
            break
    sleep(0.25)
    if locators.country == 'United States':
        pr_list = ['AK', 'AL', 'AZ', 'AR', 'DC', 'DE', 'FL', 'ID', 'IL', 'IN']
        for li in pr_list:
            locators.rand_province = random.choice(pr_list)
            driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.rand_province)
            break
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(0.25)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)
    print(f'New account now exist for {locators.first_name} {locators.last_name}. '
          f'Username is {locators.username} & associated Email ID for account is {locators.email}')
    print('')
    logger('created')


def log_in(username, password):
    print('-----------------------------Log In----------------------------------')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(2)
    driver.find_element(By.NAME, 'username').send_keys(username)
    sleep(0.25)
    driver.find_element(By.NAME, 'password').send_keys(password)
    sleep(0.25)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    print(f'{locators.first_name} {locators.last_name}, Logged in '
          f'as {locators.username} ')
    print('')


def log_out():
    print('-----------------------------Log Out----------------------------------')
    assert driver.find_element(By.ID, 'menuUserLink').is_displayed()
    sleep(0.25)
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    print('Logout Successful!!!')
    print('')
    sleep(0.25)


def validate_homepage_texts_links():
    # all text check
    print('-----------------------------Validate Home Page texts & Links----------------------------------')
    assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
    assert driver.find_element(By.ID, 'tabletsTxt').is_displayed()
    assert driver.find_element(By.ID, 'laptopsTxt').is_displayed()
    assert driver.find_element(By.ID, 'miceTxt').is_displayed()
    assert driver.find_element(By.ID, 'headphonesTxt').is_displayed()
    assert driver.find_element(By.XPATH, '//h3[contains(.,"SPECIAL OFFER")]').is_displayed()
    assert driver.find_element(By.XPATH, '//span[contains(.,"EXPLORE THE NEW DESIGN")]').is_displayed()
    assert driver.find_element(By.XPATH, '//p[contains(.,"Supremely thin, yet incredibly durable")]').is_displayed()
    assert driver.find_element(By.XPATH, '//*[contains(.,"ALL YOU WANT FROM A TABLET")]').is_displayed()
    assert driver.find_element(By.XPATH, '//h3[contains(.,"POPULAR ITEMS")]').is_displayed()
    assert driver.find_element(By.NAME, 'popular_item_16_name').is_displayed()
    assert driver.find_element(By.NAME, 'popular_item_10_name').is_displayed()
    assert driver.find_element(By.NAME, 'popular_item_21_name').is_displayed()
    assert driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed()
    assert driver.find_element(By.XPATH, '//h3[contains(.,"FOLLOW US")]').is_displayed()

    # all links check
    # driver.find_element(By.ID, 'speakersLink').click()
    driver.find_element(By.ID, 'speakersTxt').click()
    sleep(1)
    assert driver.current_url == locators.speaker_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(1)
    driver.find_element(By.ID, 'tabletsTxt').click()
    sleep(1)
    assert driver.current_url == locators.tablet_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(1)
    driver.find_element(By.ID, 'laptopsTxt').click()
    sleep(1)
    assert driver.current_url == locators.laptop_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(1)
    driver.find_element(By.ID, 'miceTxt').click()
    sleep(1)
    assert driver.current_url == locators.mice_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(1)
    driver.find_element(By.ID, 'headphonesTxt').click()
    sleep(1)
    assert driver.current_url == locators.headphone_url
    sleep(1)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.ID, 'see_offer_btn').click()
    assert driver.current_url == locators.see_offer_url
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//div/button[contains(.,"EXPLORE NOW")]').click()
    assert driver.current_url == locators.explore_now_url
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.ID, 'details_16').click()
    assert driver.current_url == locators.product_1
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.ID, 'details_10').click()
    assert driver.current_url == locators.product_2
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.ID, 'details_21').click()
    assert driver.current_url == locators.product_3
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.CLASS_NAME, 'chat').click()

    # -----------switch window code--------------
    main_page = driver.current_window_handle
    sleep(3)
    for handle in driver.window_handles:
        if handle != main_page:
            chat_page = handle
            driver.switch_to.window(chat_page)
            # change the control to chat page
            assert driver.current_url == locators.chat_url
            sleep(1)
            driver.find_element(By.ID, 'textMessage').send_keys('Hello')
            sleep(1)
            if driver.find_element(By.ID, 'btnSender').is_enabled():
                driver.find_element(By.ID, 'btnSender').click()
            else:
                print(('Alert!! Chatbox is not working'))
    sleep(6)
    driver.close()
    driver.switch_to.window(main_page)
    sleep(3)

    driver.find_element(By.NAME, 'follow_facebook').click()
    sleep(3)
    for handle in driver.window_handles:
        if handle != main_page:
            fb_page = handle
            driver.switch_to.window(fb_page)
            # change the control to fb page
            if driver.current_url != locators.fb_link:
                print('ALERT!! Broken Facebook Link')
            sleep(2)
    driver.close()
    sleep(3)
    driver.switch_to.window(main_page)
    sleep(3)

    driver.find_element(By.NAME, 'follow_twitter').click()
    sleep(3)
    for handle in driver.window_handles:
        if handle != main_page:
            tw_page = handle
            driver.switch_to.window(tw_page)
            # change the control to twitter page
            if driver.current_url != locators.twitter_link:
                print('ALERT!! Broken Twitter Link')
            sleep(2)
    driver.close()
    sleep(3)
    driver.switch_to.window(main_page)
    sleep(3)

    driver.find_element(By.NAME, 'follow_linkedin').click()
    sleep(3)
    for handle in driver.window_handles:
        if handle != main_page:
            li_page = handle
            driver.switch_to.window(li_page)
            # change the control to LinkedIn page
            if driver.current_url != locators.linkedin_link:
                print('ALERT!! Broken LinkedIn Link')

            sleep(3)
    driver.close()
    sleep(3)
    driver.switch_to.window(main_page)

    driver.find_element(By.NAME, 'go_up_btn').click()
    assert driver.current_url == locators.web_url
    sleep(3)
    print('')
    print('Main Logo is displayed & clickable')
    print('')
    print('All the texts SPEAKER | TABLETS | LAPTOP | MICE | HEADPHONES | SPECIAL OFFER TEXTS | SLIDER TEXTS | '
          'POPULAR ITEMS TEXTS |  CONTACT US | FOLLOW US | are displayed')
    print('')
    print('All "Shop Now" links for SPEAKER | TABLETS | LAPTOP | MICE | HEADPHONES and links for  SEE OFFER | '
          'EXPLORE NOW| POPULAR ITEMS VIEW DETAIL links | links  are displayed & clickable')
    print('')
    print('Chat box is Checked & Follow us links for Facebook, Twitter & Linkedin are displayed & clickable')


def top_menu_nav():
    sleep(3)
    driver.find_element(By.XPATH, '//a[contains(.,"OUR PRODUCTS")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"SPECIAL OFFER")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"POPULAR ITEMS")]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//a[contains(.,"CONTACT US")]').click()
    sleep(1)
    driver.find_element(By.ID, 'menuSearch').click()
    sleep(1)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//div[@class = "closeBtn loginPopUpCloseBtn"]').click()
    sleep(1)
    driver.find_element(By.ID, 'shoppingCartLink').click()
    sleep(2)
    driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').click()
    sleep(2)
    driver.find_element(By.ID, 'helpLink').click()
    sleep(2)
    print('')
    print('All Top Navigation Menu Links are Clickable OUR PRODUCTS | SPECIAL OFFER | POPULAR ITEMS | CONTACT US |'
          ' SEARCH ICON| USER ICON | SHOPPING CART LINK | HELP LINK ')


def contact_us_form():
    sleep(1)
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
    sleep(1)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_index(1)
    sleep(1)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(1)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.contact_sub)
    sleep(2)
    assert driver.find_element(By.ID, 'send_btnundefined').is_enabled()
    sleep(1)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(1)
    assert driver.find_element(By.XPATH,
                               '//p[contains(.,"Thank you for contacting Advantage support.")]').is_displayed()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()
    sleep(1)
    print('')
    print('CONTACT US Form working!')
    print('')


def checkout_shopping_cart():
    print('-----------------------------Check Out Shopping Cart----------------------------------')
    sleep(2)
    driver.find_element(By.ID, 'headphonesTxt').click()
    sleep(1)
    assert driver.current_url == locators.headphone_url
    sleep(1)
    product_name = driver.find_element(By.XPATH, './/a[@class="productName ng-binding"]').text
    sleep(1)
    driver.find_element(By.XPATH, './/a[@class="productName ng-binding"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(.,"ADD TO CART")]').click()
    sleep(1)
    driver.find_element(By.ID, 'checkOutPopUp').click()
    # fetching data values
    total_value = driver.find_element(By.XPATH, './/span[@class="roboto-medium totalValue ng-binding"]').text
    name = driver.find_element(By.XPATH, '//div/label[@class="ng-binding"]').text
    address = driver.find_element(By.XPATH, '//*[@id="userDetails"]/div[1]/label[1]').text
    city = driver.find_element(By.XPATH, '//*[@id="userDetails"]/div[2]/label[2]').text
    country = driver.find_element(By.XPATH, '//*[@id="userDetails"]/div[2]/label[3]').text
    state = driver.find_element(By.XPATH, '//*[@id="userDetails"]/div[2]/label[4]').text
    postal = driver.find_element(By.XPATH, '//*[@id="userDetails"]/div[2]/label[5]').text
    phone = driver.find_element(By.XPATH, '//*[@id="userDetails"]/div[3]/label').text
    sleep(1)
    driver.find_element(By.ID, 'next_btn').click()

    # ---------------------Master Card Payment-----------------------------------------
    # browser.find_element_by_xpath(".//input[@type='radio' and @value='SRF']").click()
    # driver.find_element(By.CSS_SELECTOR,'input[type="radio"][name="masterCredit"]').click()
    # driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="save_master_credit"]').click()
    # driver.find_element(By.ID,'creditCard').send_keys(locators.creditcard)
    # driver.find_element(By.XPATH, '//input[@name = "cvv_number"]').send_keys(locators.cvv)
    # driver.find_element(By.XPATH,'//input[@name = "cardholder_name"]').send_keys(locators.fullname)
    # sleep(1)
    # driver.find_element(By.XPATH,'//button[@id = "pay_now_btn_ManualPayment"]').click()
    # ---------------------Master Card Payment-----------------------------------------

    # ---------------------Safe Pay Payment-----------------------------------------

    driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="save_safepay"]').click()
    driver.find_element(By.XPATH, '//input[@name = "safepay_username"]').send_keys(locators.creditcard)
    driver.find_element(By.XPATH, '//input[@name = "safepay_password"]').send_keys(locators.cvv)
    sleep(1)
    driver.find_element(By.XPATH, '//button[@id = "pay_now_btn_SAFEPAY"]').click()
    sleep(3)
    assert driver.find_element(By.XPATH, './/span[@class="roboto-regular ng-scope"]').is_displayed()
    track_num = driver.find_element(By.ID, 'trackingNumberLabel').text
    order_num = driver.find_element(By.ID, 'orderNumberLabel').text

    # assert data values

    assert driver.find_element(By.XPATH, f'//div[contains(.,"{name}")]').is_displayed()
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{address}")]').is_displayed()
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{city}")]').is_displayed()
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{country}")]').is_displayed()
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{state}")]').is_displayed()
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{postal}")]').is_displayed()
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{phone}")]').is_displayed()
    # assert driver.find_element(By.XPATH,f'//div[contains(.,"{datetime.datetime.now().strftime
    # ("%d/%-m/%Y")}")]').is_displayed()
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{total_value}")]').is_displayed()
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
    sleep(1)
    assert driver.find_element(By.XPATH, f'//tr[contains(.,"{order_num}")]').is_displayed()
    assert driver.find_element(By.XPATH, f'//tr[contains(.,"{product_name}")]').is_displayed()

    print(f'Order placed for {name}.The delivery address is {address}, {city} {state}, {country} , {postal}. '
          f'Customer can be reach at {phone}.')
    print('')
    print(f'Customer order : {product_name} & total cost is {total_value}.')
    print('')
    print(f'The order number is {order_num} & tracking number is {track_num}.')
    print('')
    driver.find_element(By.LINK_TEXT, 'REMOVE').click()
    sleep(1)
    driver.find_element(By.XPATH, '//button[contains(.,"YES")]').click()
    sleep(1)
    print(f'Order Cancel for {name}, PRODUCT : {product_name}. CUSTOMER CANCELLED THE ORDER!!!. ')
    assert driver.find_element(By.XPATH, '//div//label[contains(., " - No orders - ")]').is_displayed()
    assert driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_enabled()
    driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').click()
    sleep(1)
    print('')

def edit_user():
    print('--------------------------Edit User---------------------------------')
    sleep(2)
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My account")]').click()
    sleep(0.25)
    name = driver.find_element(By.XPATH, '//div/label[@class="ng-binding"]').text
    sleep(0.25)
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{name}")]').is_displayed
    sleep(0.25)
    driver.find_element(By.XPATH,'//h3/a[contains(.,"Edit")]').click()
    sleep(3)
    #-------------------Change Deatils for Email & Password-------------
    # driver.find_element(By.NAME,'emailAccountDetails').clear()
    # driver.find_element(By.NAME,'emailAccountDetails').send_keys('newuser@gmail.com')
    # driver.find_element(By.LINK_TEXT,'Change password').click()
    # driver.find_element(By.NAME,'old_passwordAccountDetails').click()
    # driver.find_element(By.NAME,'old_passwordAccountDetails').send_keys(locators.password)
    # driver.find_element(By.NAME,'new_passwordAccountDetails').click()
    # driver.find_element(By.NAME,'new_passwordAccountDetails').send_keys('Kk12345')
    # driver.find_element(By.NAME,'confirm_new_passwordAccountDetails').click()
    # driver.find_element(By.NAME,'confirm_new_passwordAccountDetails').send_keys('Kk12345')
    #----------------------------------------------------------------------------------------
    driver.find_element(By.NAME,'first_nameAccountDetails').click()
    sleep(1)
    driver.find_element(By.NAME, 'first_nameAccountDetails').clear()
    sleep(1)
    driver.find_element(By.NAME,'first_nameAccountDetails').send_keys('Anna')
    sleep(1)
    new_name = driver.find_element(By.NAME,'first_nameAccountDetails').text
    sleep(1)
    driver.find_element(By.ID,'save_btnundefined').click()
    sleep(1)
    assert driver.current_url == locators.my_account_url
    print('Edit Successful!!!.')
    print('')


def delete_user():
    print('--------------------------Delete the User----------------------------')
    sleep(1)
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My orders")]').click()
    sleep(1)
    assert driver.find_element(By.XPATH, '//div//label[contains(., " - No orders - ")]').is_displayed()
    assert driver.find_element(By.LINK_TEXT, 'CONTINUE SHOPPING').is_enabled()
    sleep(1)
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"My account")]').click()
    new_name = driver.find_element(By.XPATH, '//div/label[@class="ng-binding"]').text
    sleep(0.25)
    assert driver.find_element(By.XPATH, f'//div[contains(.,"{new_name}")]').is_displayed()
    print(f'Name changed from {locators.first_name} {locators.last_name} to {new_name}.')
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="category_laptops"]').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'input[type="checkbox"][name="category_mice"]').click()
    sleep(1)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    driver.find_element(By.XPATH,'//button/div[contains(.,"Delete Account")]').click()
    sleep(2)
    driver.find_element(By.XPATH,'//div/div[contains(.,"yes")]').click()
    sleep(3)
    logger('Deleted')
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(3)
    driver.find_element(By.NAME,'username').click()
    sleep(0.25)
    driver.find_element(By.NAME,'username').send_keys(locators.username)
    sleep(0.25)
    driver.find_element(By.NAME,'password').click()
    sleep(0.25)
    driver.find_element(By.NAME,'password').send_keys(locators.password)
    sleep(0.25)
    driver.find_element(By.ID,'sign_in_btnundefined').click()
    sleep(0.25)
    assert driver.current_url == locators.web_url
    sleep(0.25)
    assert driver.find_element(By.ID,'signInResultMessage').is_displayed()
    sleep(1)
    driver.find_element(By.XPATH, '//div[@class = "closeBtn loginPopUpCloseBtn"]').click()
    print('User Deleted Successfully')
    print('')


def tearDown():
    if driver is not None:
        print('-----------------~~~~~~-------------------')
        print(f'This AOS Test Complete at : {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
              f' on {datetime.datetime.today().strftime("%A")}')
        sleep(0.25)
        driver.close()
        driver.quit()


def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.username}\t'
          f'{locators.password}\t'
          f'{locators.username}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()
