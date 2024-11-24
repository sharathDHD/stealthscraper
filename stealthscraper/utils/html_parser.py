from bs4 import BeautifulSoup
from typing import Dict, Any, List

class HTMLParser:
    def extract_metadata(self, soup: BeautifulSoup, source_url: str, status_code: int) -> Dict[str, Any]:
        metadata = {
            "title": self._get_title(soup),
            "description": self._get_meta_content(soup, "description"),
            "language": self._get_language(soup),
            "keywords": self._get_meta_content(soup, "keywords"),
            "robots": self._get_meta_content(soup, "robots"),
            "ogTitle": self._get_og_content(soup, "title"),
            "ogDescription": self._get_og_content(soup, "description"),
            "ogUrl": self._get_og_content(soup, "url"),
            "ogImage": self._get_og_content(soup, "image"),
            "ogLocaleAlternate": self._get_og_locale_alternate(soup),
            "ogSiteName": self._get_og_content(soup, "site_name"),
            "sourceURL": source_url,
            "statusCode": status_code
        }
        return {k: v for k, v in metadata.items() if v is not None}

    def _get_title(self, soup: BeautifulSoup) -> str:
        title_tag = soup.find('title')
        return title_tag.string if title_tag else None

    def _get_meta_content(self, soup: BeautifulSoup, name: str) -> str:
        meta_tag = soup.find('meta', attrs={'name': name})
        return meta_tag.get('content') if meta_tag else None

    def _get_language(self, soup: BeautifulSoup) -> str:
        html_tag = soup.find('html')
        return html_tag.get('lang') if html_tag else None

    def _get_og_content(self, soup: BeautifulSoup, property: str) -> str:
        og_tag = soup.find('meta', attrs={'property': f'og:{property}'})
        return og_tag.get('content') if og_tag else None

    def _get_og_locale_alternate(self, soup: BeautifulSoup) -> List[str]:
        og_locale_tags = soup.find_all('meta', attrs={'property': 'og:locale:alternate'})
        return [tag.get('content') for tag in og_locale_tags if tag.get('content')] 