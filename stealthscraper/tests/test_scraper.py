import unittest
from stealthscraper import StealthScraper

class TestStealthScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = StealthScraper()

    def test_successful_scrape(self):
        url = "https://example.com"
        result = self.scraper.scrape(url)
        
        self.assertTrue(result["success"])
        self.assertIn("data", result)
        self.assertIn("markdown", result["data"])
        self.assertIn("html", result["data"])
        self.assertIn("metadata", result["data"])

    def test_failed_scrape(self):
        url = "https://nonexistent-website-xyz.com"
        result = self.scraper.scrape(url)
        
        self.assertFalse(result["success"])
        self.assertIn("error", result)

if __name__ == '__main__':
    unittest.main() 