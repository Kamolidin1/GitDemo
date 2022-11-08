from selenium.webdriver.common.by import By
class BuyPage:
    def __init__(self, driver):
       self.driver = driver

    add_to_cart = (By.CSS_SELECTOR, "a[aria-label='Add “Album” to your cart']")
    shopping_cart = (By.CSS_SELECTOR, "a[title='View cart']")
    coupon = (By.CSS_SELECTOR, "input[name='coupon_code']")
    apply_coupon = (By.XPATH, "//button[@name='apply_coupon']")
    checkout = (By.CSS_SELECTOR, "a[class='checkout-button button alt wc-forward wp-element-button']")

    def get_login_page(self):
        return self.driver.get("http://shopping.beeyor.com/shop")

    def get_add_to_cart(self):
        return self.driver.find_element(*BuyPage.add_to_cart)

    def get_shopping_cart(self):
        return self.driver.find_element(*BuyPage.shopping_cart)

    def get_coupon(self):
        return self.driver.find_element(*BuyPage.coupon)

    def get_apply_coupon(self):
        return self.driver.find_element(*BuyPage.apply_coupon)

    def get_checkout(self):
        return self.driver.find_element(*BuyPage.checkout)