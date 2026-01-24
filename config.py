"""
Configuration file for Startup India Scraper
"""

# Scraping Configuration
BASE_URL = "https://www.startupindia.gov.in/content/sih/en/search.html?roles=Startup&page="
START_PAGE = 1
END_PAGE = 10  # Adjust this to scrape more pages

# Browser Configuration
HEADLESS_MODE = True  # Set to False to see browser in action
WAIT_TIMEOUT = 20  # Seconds to wait for elements
PAGE_LOAD_DELAY = 3  # Seconds to wait after loading page
SCROLL_DELAY = 2  # Seconds to wait after scrolling

# Data Export Configuration
EXPORT_CSV = True
EXPORT_EXCEL = True
EXPORT_JSON = True

# Output filename pattern
OUTPUT_FILENAME_PATTERN = "startup_leads_{timestamp}"

# Scraping filters (optional)
FILTER_BY_STAGE = []  # e.g., ['Ideation', 'Scaling'] or [] for all
FILTER_BY_SECTOR = []  # e.g., ['AI', 'FinTech'] or [] for all
FILTER_BY_STATE = []  # e.g., ['Karnataka', 'Maharashtra'] or [] for all

# Rate limiting (be respectful to the server)
DELAY_BETWEEN_PAGES = 2  # Seconds between page requests
DELAY_BETWEEN_PROFILES = 1  # Seconds between profile requests

# User Agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Detailed scraping (slower but more data)
SCRAPE_PROFILE_DETAILS = False  # Set to True to scrape individual startup profiles
