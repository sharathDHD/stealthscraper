from setuptools import setup, find_packages

setup(
    name="stealthscraper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "cloudscraper>=1.2.71",
        "beautifulsoup4>=4.12.0",
        "html2text>=2020.1.16",
        "requests>=2.31.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A web scraper that bypasses Cloudflare protection",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/stealthscraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 