import cloudscraper
from bs4 import BeautifulSoup
import html2text
from typing import Dict, Any, Optional
from .utils.html_parser import HTMLParser

class StealthScraper:
    def __init__(self, timeout: int = 30):
        self.scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'chrome',
                'platform': 'windows',
                'mobile': False
            },
            delay=10
        )
        self.timeout = timeout
        self.parser = HTMLParser()
        self.html2text = html2text.HTML2Text()
        self.html2text.ignore_links = False
        self.html2text.ignore_images = False

    def scrape(self, url: str) -> Dict[str, Any]:
        try:
            response = self.scraper.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            
            metadata = self.parser.extract_metadata(soup, url, response.status_code)
            markdown = self.html2text.handle(html_content)

            return {
                "success": True,
                "data": {
                    "markdown": markdown,
                    "html": html_content,
                    "metadata": metadata
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            } 