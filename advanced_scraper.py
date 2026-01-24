"""
Advanced Startup India Scraper with Enhanced Features
Includes AI-powered data enrichment, filters, and detailed profile scraping
"""

import time
import json
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd
import config


class AdvancedStartupScraper:
    def __init__(self, headless=None):
        """Initialize the advanced scraper"""
        if headless is None:
            headless = config.HEADLESS_MODE
        
        self.startups_data = []
        self.detailed_profiles = []
        
        # Setup Chrome options
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument(f"user-agent={config.USER_AGENT}")
        chrome_options.add_argument("--window-size=1920,1080")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, config.WAIT_TIMEOUT)
        
    def apply_filters(self):
        """Apply filters on the search page"""
        try:
            # Wait for filter section to load
            time.sleep(2)
            
            # Click on filters if needed
            # Extract startup details
            startups = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/content/sih/en/profile.Startup']")
            for startup in startups:
                name = startup.text
                link = startup.get_attribute('href')
                self.driver.get(link)
                time.sleep(2)
                try:
                    website = self.driver.find_element(By.CSS_SELECTOR, "a[href*='http']").get_attribute('href')
                except NoSuchElementException:
                    website = None
                try:
                    phone = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Phone')]/following-sibling::div").text
                except NoSuchElementException:
                    phone = None
                try:
                    email = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Email')]/following-sibling::div").text
                except NoSuchElementException:
                    email = None
                self.startups_data.append({'name': name, 'website': website, 'phone': phone, 'email': email})
                self.driver.back()
            # This is a placeholder - actual implementation depends on website structure
            print("Filters can be applied through URL parameters")
            
        except Exception as e:
            print(f"Error applying filters: {e}")
    
    def extract_startup_card_data(self, card_element):
        """Extract data from a startup card element"""
        try:
            startup_data = {
                'company_name': '',
                'stage': '',
                'city': '',
                'state': '',
                'location': '',
                'sector': '',
                'profile_url': '',
                'is_dpiit_recognized': False,
                'is_tax_exempt': False,
                'scraped_at': datetime.now().isoformat()
            }
            
            # Get the link
            link = card_element.find_element(By.TAG_NAME, 'a')
            startup_data['profile_url'] = link.get_attribute('href')
            
            # Get text content
            text = card_element.text.strip()
            lines = [line.strip() for line in text.split('\n') if line.strip()]
            
            if len(lines) >= 1:
                startup_data['company_name'] = lines[0]
            
            # Parse stage and location from second line
            if len(lines) >= 2:
                second_line = lines[1]
                
                # Extract stage
                stages = ['Ideation', 'Validation', 'Early Traction', 'Scaling', 'Profitable']
                for stage in stages:
                    if stage in second_line:
                        startup_data['stage'] = stage
                        break
                
                # Extract location (after stage)
                location_text = second_line
                if startup_data['stage']:
                    location_text = second_line.replace(startup_data['stage'], '').strip()
                
                startup_data['location'] = location_text
                
                # Try to split city and state
                if ',' in location_text:
                    parts = location_text.split(',')
                    startup_data['city'] = parts[0].strip()
                    startup_data['state'] = parts[1].strip() if len(parts) > 1 else ''
            
            # Extract sector from third line
            if len(lines) >= 3:
                startup_data['sector'] = lines[2]
            
            return startup_data
            
        except Exception as e:
            print(f"Error extracting card data: {e}")
            return None
    
    def scrape_page_enhanced(self, page_number):
        """Enhanced page scraping with better data extraction"""
        url = f"{config.BASE_URL}{page_number}"
        print(f"Scraping page {page_number}: {url}")
        
        try:
            self.driver.get(url)
            time.sleep(config.PAGE_LOAD_DELAY)
            
            # Wait for content to load
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/content/sih/en/profile.Startup']")))
            
            # Scroll to load all content
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(config.SCROLL_DELAY)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height
            
            # Find all startup links
            startup_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/content/sih/en/profile.Startup']")
            
            print(f"Found {len(startup_links)} startups on page {page_number}")
            
            for link in startup_links:
                try:
                    text = link.text.strip()
                    profile_url = link.get_attribute('href')
                    
                    if not text or not profile_url:
                        continue
                    
                    # Skip duplicates
                    if any(s['profile_url'] == profile_url for s in self.startups_data):
                        continue
                    
                    startup_data = {
                        'company_name': '',
                        'stage': '',
                        'location': '',
                        'city': '',
                        'state': '',
                        'sector': '',
                        'profile_url': profile_url,
                        'page_number': page_number,
                        'scraped_at': datetime.now().isoformat()
                    }
                    
                    # Parse the text content
                    lines = [line.strip() for line in text.split('\n') if line.strip()]
                    
                    if len(lines) >= 1:
                        startup_data['company_name'] = lines[0]
                    
                    if len(lines) >= 2:
                        second_line = lines[1]
                        stages = ['Ideation', 'Validation', 'Early Traction', 'Scaling', 'Profitable']
                        
                        for stage in stages:
                            if stage in second_line:
                                startup_data['stage'] = stage
                                location_text = second_line.replace(stage, '').strip()
                                startup_data['location'] = location_text
                                
                                # Split city and state
                                if ',' in location_text:
                                    parts = location_text.split(',')
                                    startup_data['city'] = parts[0].strip()
                                    startup_data['state'] = parts[1].strip() if len(parts) > 1 else ''
                                break
                    
                    if len(lines) >= 3:
                        startup_data['sector'] = lines[2]
                    
                    # Apply filters if configured
                    if self.should_include(startup_data):
                        self.startups_data.append(startup_data)
                
                except Exception as e:
                    print(f"Error parsing startup: {e}")
                    continue
            
            return len(startup_links)
            
        except Exception as e:
            print(f"Error scraping page {page_number}: {e}")
            return 0
    
    def should_include(self, startup_data):
        """Check if startup matches filter criteria"""
        # Stage filter
        if config.FILTER_BY_STAGE and startup_data.get('stage'):
            if startup_data['stage'] not in config.FILTER_BY_STAGE:
                return False
        
        # Sector filter
        if config.FILTER_BY_SECTOR and startup_data.get('sector'):
            if not any(sector.lower() in startup_data['sector'].lower() for sector in config.FILTER_BY_SECTOR):
                return False
        
        # State filter
        if config.FILTER_BY_STATE and startup_data.get('state'):
            if startup_data['state'] not in config.FILTER_BY_STATE:
                return False
        
        return True
    
    def scrape_detailed_profile(self, profile_url):
        """Scrape detailed information from startup profile page"""
        try:
            print(f"Scraping profile: {profile_url}")
            self.driver.get(profile_url)
            time.sleep(config.DELAY_BETWEEN_PROFILES)
            
            details = {
                'profile_url': profile_url,
                'description': '',
                'website': '',
                'email': '',
                'phone': '',
                'founded_year': '',
                'team_size': '',
                'founders': [],
                'social_media': {},
                'tags': [],
                'recognition_number': ''
            }
            
            # Extract page content
            page_text = self.driver.find_element(By.TAG_NAME, 'body').text
            
            # Try to find email
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, page_text)
            if emails:
                details['email'] = emails[0]
            
            # Try to find phone
            phone_pattern = r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}'
            phones = re.findall(phone_pattern, page_text)
            if phones:
                details['phone'] = phones[0]
            
            # Try to find website
            try:
                website_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='http']")
                for link in website_links:
                    href = link.get_attribute('href')
                    if 'startupindia.gov.in' not in href and 'mailto:' not in href:
                        details['website'] = href
                        break
            except:
                pass
            
            return details
            
        except Exception as e:
            print(f"Error scraping profile details: {e}")
            return {}
    
    def scrape_all(self):
        """Main scraping method"""
        print(f"Starting scraping from page {config.START_PAGE} to {config.END_PAGE}")
        
        for page in range(config.START_PAGE, config.END_PAGE + 1):
            count = self.scrape_page_enhanced(page)
            
            if count == 0:
                print(f"No startups found on page {page}. Stopping.")
                break
            
            print(f"Total collected: {len(self.startups_data)} startups")
            time.sleep(config.DELAY_BETWEEN_PAGES)
        
        # Scrape detailed profiles if enabled
        if config.SCRAPE_PROFILE_DETAILS and self.startups_data:
            print("\nScraping detailed profiles...")
            for i, startup in enumerate(self.startups_data[:10]):  # Limit to first 10 for demo
                details = self.scrape_detailed_profile(startup['profile_url'])
                self.detailed_profiles.append({**startup, **details})
                print(f"Progress: {i+1}/10")
        
        return self.startups_data
    
    def save_data(self):
        """Save scraped data to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if config.EXPORT_CSV:
            filename = f"{config.OUTPUT_FILENAME_PATTERN.format(timestamp=timestamp)}.csv"
            df = pd.DataFrame(self.startups_data)
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            print(f"CSV saved: {filename}")
        
        if config.EXPORT_EXCEL:
            filename = f"{config.OUTPUT_FILENAME_PATTERN.format(timestamp=timestamp)}.xlsx"
            df = pd.DataFrame(self.startups_data)
            df.to_excel(filename, index=False, engine='openpyxl')
            print(f"Excel saved: {filename}")
        
        if config.EXPORT_JSON:
            filename = f"{config.OUTPUT_FILENAME_PATTERN.format(timestamp=timestamp)}.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.startups_data, f, indent=2, ensure_ascii=False)
            print(f"JSON saved: {filename}")
    
    def generate_report(self):
        """Generate a summary report"""
        if not self.startups_data:
            return "No data collected"
        
        df = pd.DataFrame(self.startups_data)
        
        report = {
            'total_startups': len(df),
            'by_stage': df['stage'].value_counts().to_dict() if 'stage' in df.columns else {},
            'by_sector': df['sector'].value_counts().head(15).to_dict() if 'sector' in df.columns else {},
            'by_state': df['state'].value_counts().head(15).to_dict() if 'state' in df.columns else {},
            'top_cities': df['city'].value_counts().head(15).to_dict() if 'city' in df.columns else {}
        }
        
        print("\n" + "="*70)
        print("SCRAPING REPORT")
        print("="*70)
        print(json.dumps(report, indent=2))
        print("="*70)
        
        return report
    
    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()


def main():
    print("="*70)
    print("ADVANCED STARTUP INDIA LEAD GENERATION SCRAPER")
    print("="*70)
    print(f"Configuration:")
    print(f"  - Pages: {config.START_PAGE} to {config.END_PAGE}")
    print(f"  - Headless: {config.HEADLESS_MODE}")
    print(f"  - Detailed profiles: {config.SCRAPE_PROFILE_DETAILS}")
    print("="*70)
    
    scraper = AdvancedStartupScraper()
    
    try:
        # Scrape data
        scraper.scrape_all()
        
        # Generate report
        scraper.generate_report()
        
        # Save data
        print("\nSaving data...")
        scraper.save_data()
        
        print("\n" + "="*70)
        print("SCRAPING COMPLETED SUCCESSFULLY!")
        print(f"Total startups collected: {len(scraper.startups_data)}")
        print("="*70)
        
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        scraper.close()


if __name__ == "__main__":
    main()
