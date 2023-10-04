from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """Testing new visitor."""

    def setUp(self) -> None:
        """Setup firefox browser."""
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        """Exit from browser."""
        self.browser.quit()

    def test_can_start_a_list_retrieve_it_later(self):
        """Testing start list and get them later."""
        self.browser.get('http://localhost:8000')

        # Makes sure by looking at the title that
        # it is definitely on the to-do page
        self.assertIn('To-Do', self.browser.title)
        self.fail('End test')


    # Tries to add 'buy the book' to the to-do list

    # Press 'Enter' to see the result

    # Sees the updated list witch contain '1. buy the book'

    # Text area prompts you to enter another item
    # User enters 'read this book' and press 'Enter'

    # Page is being updated and now containing both items

    # The user checks whether the site remembers her affairs.
    # The site has generated a specific URL address for it,
    # about which a message appears.

    # User click on URL and see his to-do list.

    # Say bye-bye to tomorrow.

if __name__ == '__main__':
    unittest.main(warnings='ignore')