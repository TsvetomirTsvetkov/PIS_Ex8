import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        # Create an instance of the Chrome driver
        self.driver = webdriver.Chrome()
        # Maximize the window
        self.driver.maximize_window()
        # Open the page
        self.driver.get('file:///home/sktuan/Documents/education/tu_university/pis/PIS_Ex8/src/main/index.html')

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_registration_form_fail_without_password(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('test@test.com')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Wait for the "Thank You" container to be visible
        # try:
        #     thank_you_container = WebDriverWait(self.driver, 3).until(
        #         EC.presence_of_element_located((By.ID, 'thankYouContainer'))
        #     )
        #     self.assertTrue(thank_you_container.is_displayed(), "Thank You container is visible!")
        # except Exception as e:
        #     self.fail(f"Thank You container is not visible. Exception: {e}")


if __name__ == '__main__':
    unittest.main()
