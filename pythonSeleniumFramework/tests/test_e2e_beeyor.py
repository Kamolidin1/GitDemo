import pytest
from selenium.webdriver.common.by import By

from pageObjects.BillingInfo import BillingInfo
from pageObjects.BuyPage import BuyPage
from testLoginData.BillingData import BillingData
from utilities.BaseClass import BaseClass

class TestE2E(BaseClass):
    def test_end_to_end(self, data_info):
        shopping = BuyPage(self.driver)
        shopping.get_login_page()
        shopping.get_add_to_cart().click()
        shopping.get_shopping_cart().click()
        shopping.get_coupon().send_keys(data_info["coupon"])
        shopping.get_apply_coupon().click()
        shopping.get_checkout().click()
        billing = BillingInfo(self.driver)
        billing.get_firstname().send_keys(data_info["firstname"])
        billing.get_lastname().send_keys(data_info["lastname"])
        billing.get_billing_address().send_keys(data_info["address"])
        billing.get_billing_city().send_keys(data_info["city"])
        billing.get_postcode().send_keys(data_info["postcode"])
        billing.get_phone().send_keys(data_info["phone"])
        billing.get_email().send_keys(data_info["email"])
        billing.get_frame1()
        billing.get_cardnumber().send_keys(data_info["cardnumber"])
        billing.get_homewindow()
        billing.get_frame2()
        billing.get_expirationdate().send_keys(data_info["expirationdate"])
        billing.get_homewindow()
        billing.get_frame3()
        billing.get_securitycode().send_keys(data_info["securitycode"])
        billing.get_homewindow()
        billing.get_placeorder().click()

    @pytest.fixture(params=BillingData.test_info)
    def data_info(self, request):
        return request.param