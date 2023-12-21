import unittest
from register.test_registration_form import TestRegistrationForm


def run_tests():
    # Create a test suite
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRegistrationForm)
    suite = unittest.TestSuite([test_suite])

    # Run the tests
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Check results
    if result.wasSuccessful():
        print("All the tests have passed!")
    else:
        print("Some of the tests have failed.")


if __name__ == '__main__':
    run_tests()
