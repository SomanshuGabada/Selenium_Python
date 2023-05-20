from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True) #to avoid closing browser after each function
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# driver.set_window_size(1000,1000)

def registration(name,email,password):
    print("------------------------------------------------------")
    print('Initiating Registration...')
    driver.get("https://automation.credence.in/shop")
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "name").send_keys(name)
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "password-confirm").send_keys(password)
    driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    print("Registration Done Succesfully with credentials")
    print(f'''name => {name}\nemail => {email}\npassword => {password}''')
    print("------------------------------------------------------")
    login(email,password)

def login(email,password):
    print("------------------------------------------------------")
    print('initiating login...')
    driver.find_element(By.LINK_TEXT,"Login").click()
    driver.find_element(By.ID , "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    print("Login Succesful!")
    print(f"""Credentials used:\nemail => {email}\npassword => {password}""")
    print("------------------------------------------------------")
    add_to_cart()

def add_to_cart():
    print("------------------------------------------------------")
    print("initiating module: add_to_cart")
    driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/ps4.jpg']").click()
    print("adding product to cart...")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    print("product added to cart succesfully ! ! !")
    print("------------------------------------------------------")
    cart_value()

def cart_value():
    product1 = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr[1]/td[2]").text
    price1 = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr[1]/td[4]").text
    subtotal = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[2]/td[4]").text
    tax = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[3]/td[4]").text
    total = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr[4]/td[4]").text
    print("------------------------------------------------------")
    print(f"""{product1} => {price1}\nsubtotal => {subtotal}\ntax => {tax}\ntotal => {total}""")
    print("------------------------------------------------------")
    click_proceed_to_checkout()

def click_proceed_to_checkout():
    driver.find_element(By.CLASS_NAME,"btn.btn-success.btn-lg").click()
    checkout()

def checkout():
    print("------------------------------------------------------")
    print("initiating checkout")
    print("Filling Checkout Form ...")
    driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys(first_name)
    driver.find_element(By.XPATH, "//input[@name='last_name']").send_keys(last_name)
    driver.find_element(By.XPATH, "//input[@name='phone']").send_keys(phone)
    driver.find_element(By.XPATH, "//textarea[@name='address']").send_keys(address)
    driver.find_element(By.XPATH, "//input[@name='zip']").send_keys(zip)
    select = Select(driver.find_element(By.XPATH, "//select[@name='state']"))
    select.select_by_index(1)
    print("Checkout Form Filled Successfully!")
    print("------------------------------------------------------")
    print("Inserting Card Details")
    driver.find_element(By.XPATH,"//input[@name='owner']").send_keys(card_owner)
    driver.find_element(By.XPATH, "//input[@name='cvv']").send_keys(cvv)
    for i in cardNumber:
        driver.find_element(By.XPATH, "//input[@name='cardNumber']").send_keys(i)
    select = Select(driver.find_element(By.XPATH,"//select[@name='exp_year']"))
    select.select_by_visible_text(exp_year)
    select = Select(driver.find_element(By.XPATH, "//select[@name='exp_month']"))
    select.select_by_visible_text(exp_month)
    driver.find_element(By.XPATH,"//button[@id='confirm-purchase']").click()
    print("initiating [Continue to Checkout]")
    current_url = driver.current_url
    if current_url == 'https://automation.credence.in/shop':
        print('''
        \t\t\tThank you
        Your order has been placed successfully
        ''')
    print("------------------------------------------------------")



name = "unknown11111"
email = "unknown11111@gmail.com"
password = "123456789"

first_name = 'Unidentified'
last_name = 'Unidentified'
phone = 1234567890
address = 'Unidentified Unidentified Unidentified Unidentified'
zip = 121212

card_owner = "Unidentified Unidentified"
cvv = 321
cardNumber = "4716108999716531"
exp_year = "2023"
exp_month = "January"
registration(name,email,password)
'''
Visa
4716108999716531
321
'''

#/html/body/div/table/tbody/tr/td[4]




