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

    def test_registration_form_success(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('example@example.com')
        password.send_keys('password123')

        # Get the initial URL
        initial_url = self.driver.current_url

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Assert that the current URL after submission is the same as the initial URL
        current_url = self.driver.current_url
        self.assertEqual(initial_url, current_url, "Redirected to the same page after form submission")

    def test_registration_form_password_short(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('example@example.com')
        password.send_keys('1234')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Password must be at least 8 characters long", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for password shorter than expected")

    def test_registration_form_password_long(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('example@example.com')
        password.send_keys('123456789123456789123456789123456789')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Password must be at most 30 characters long", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for password longer than expected")

    def test_registration_form_password_empty(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('example@example.com')
        password.send_keys('')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Password cannot be empty", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for missing password")

    def test_registration_form_email_empty(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('')
        password.send_keys('password123')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Email cannot be empty", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for missing email")

    def test_registration_form_email_at_after_dot(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('exampleexample.@com')
        password.send_keys('password123')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Invalid email: '.' appears before '@'", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for '@' after '.'")

    def test_registration_form_email_multiple_ats(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('example@@example.com')
        password.send_keys('password123')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Invalid email: Multiple '@' symbols", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for multiple '@' symbols")

    def test_registration_form_email_missing_at(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('exampleexample.com')
        password.send_keys('password123')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Invalid email: Missing '@' or '.'", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for missing '@'")

    def test_registration_form_email_missing_dot(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('example@examplecom')
        password.send_keys('password123')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Invalid email: Missing '@' or '.'", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for missing '.'")

    def test_registration_form_email_space(self):
        # Get fields
        email = self.driver.find_element(By.ID, 'email')
        password = self.driver.find_element(By.ID, 'password')
        submit = self.driver.find_element(By.ID, 'submit')

        # Fill in the form fields
        email.send_keys('example@ example.com')
        password.send_keys('password123')

        # Click the submit button
        submit.click()
        time.sleep(1)

        # Check for an alert message
        try:
            alert = self.driver.switch_to.alert
            self.assertIsNotNone(alert, "Alert not found")
            alert_text = alert.text
            self.assertEqual(alert_text, "Invalid email: Contains space", "Unexpected alert message")
            alert.accept()
        except Exception:
            self.fail("No alert detected for empty space")


if __name__ == '__main__':
    unittest.main()
