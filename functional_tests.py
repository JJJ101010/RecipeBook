from selenium import webdriver
import unittest

class BasicVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_click_a_link_to_a_recipe(self):
        #open the site
        self.browser.get('http://localhost:8000')

        #see the homepage title
        self.assertIn('Recipe Book', self.browser.title)
        self.fail('Finish the test!')

        #see the list of recipes in a column

        #clicking on a recipe name pulls up that recipe

if __name__ == '__main__':
    unittest.main(warnings='ignore')