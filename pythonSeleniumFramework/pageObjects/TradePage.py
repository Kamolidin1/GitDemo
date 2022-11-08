
from selenium.webdriver.common.by import By
class TradePage:

    def __init__(self, driver):
        self.driver = driver
    trade_button = (By.XPATH, "//button[@data-testid='trade-page-button']")
    symbol = (By.ID, "navigation-symbol-search")
    symbol_lookup = (By.CSS_SELECTOR, "li[data-testid='symbol-search-dropdown:AAPL']")
    side = (By.XPATH, "//button[@direction='buy']")
    quantity = (By.XPATH, "//input[@type='number']")
    review = (By.CSS_SELECTOR, '#review-order-button')
    send = (By.CSS_SELECTOR, '#send-order-button')
    notification = (By.XPATH, "//div[text()= 'Notifications']")

    def get_trade_button(self):
        return self.driver.find_element(*TradePage.trade_button)

    def get_symbol(self):
        return self.driver.find_element(*TradePage.symbol)

    def get_symbol_lookup(self):
        return self.driver.find_element(*TradePage.symbol_lookup)

    def get_side(self):
        return self.driver.find_element(*TradePage.side)

    def get_quantity(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_quantity_input(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_review(self):
        return self.driver.find_element(*TradePage.review)

    def get_send(self):
        return self.driver.find_element(*TradePage.send)

    def get_notification(self):
        return self.driver.find_element(*TradePage.notification)

    def get_order_confirmation(self):

        original_confirmation = []
        original_message = [
            self.driver.find_element(By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]").text]
        print(original_message)
        for records in original_message:
            original_confirmation.append(records)
        print(original_confirmation)
        assert original_message == original_confirmation
        return original_message
