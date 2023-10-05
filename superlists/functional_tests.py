from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
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

        # Makes sure by looking at the title and header that
        # it is definitely on the to-do page
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # Prompts you enter items
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-fo item'
        )

        # Tries to add 'buy the book' to the to-do list
        inputbox.send_keys('Buy \'Little Dorrit\' by Charles Dickens')
        # Press 'Enter' to see the result
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Sees the updated list witch contain '1. buy the book'
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_element(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Buy \'Little Dorrit\' byCharles Dickens' for row in rows)
        )

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