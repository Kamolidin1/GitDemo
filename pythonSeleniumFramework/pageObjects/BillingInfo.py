from selenium.webdriver.common.by import By


class BillingInfo:
    def __init__(self, driver):
        self.driver = driver

    firstname = (By.ID, "billing_first_name")
    lastname = (By.ID, "billing_last_name")
    billing_address = (By.ID, "billing_address_1")
    billing_city = (By.ID, "billing_city")
    postcode = (By.ID, "billing_postcode")
    phone = (By.ID, "billing_phone")
    email = (By.ID, "billing_email")
    cardnumber = (By.XPATH, "//input[@aria-label='Credit or debit card number']")
    expirationdate = (By.CSS_SELECTOR, "input[aria-label='Credit or debit card expiration date']")
    securitycode = (By.CSS_SELECTOR, "input[aria-label='Credit or debit card CVC/CVV']")
    placeorder = (By.ID, "place_order")

    def get_firstname(self):
        return self.driver.find_element(*BillingInfo.firstname)

    def get_lastname(self):
        return self.driver.find_element(*BillingInfo.lastname)

    def get_billing_address(self):
        return self.driver.find_element(*BillingInfo.billing_address)

    def get_billing_city(self):
        return self.driver.find_element(*BillingInfo.billing_city)

    def get_postcode(self):
        return self.driver.find_element(*BillingInfo.postcode)

    def get_phone(self):
        return self.driver.find_element(*BillingInfo.phone)

    def get_email(self):
        return self.driver.find_element(*BillingInfo.email)

    def get_frame1(self):
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, "//iframe[@title='Secure card number input frame']"))
        return

    def get_cardnumber(self):
        return self.driver.find_element(*BillingInfo.cardnumber)

    def get_expirationdate(self):
        return self.driver.find_element(*BillingInfo.expirationdate)

    def get_securitycode(self):
        return self.driver.find_element(*BillingInfo.securitycode)

    def get_placeorder(self):
        return self.driver.find_element(*BillingInfo.placeorder)

    def get_frame2(self):
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, "//iframe[@title='Secure expiration date input frame']"))
        return

    def get_frame3(self):
        self.driver.switch_to.frame(
            self.driver.find_element(By.XPATH, "//iframe[@title='Secure CVC input frame']"))
        return

    def get_homewindow(self):
        HomeWindow = self.driver.window_handles
        self.driver.switch_to.window(HomeWindow[0])
        return
