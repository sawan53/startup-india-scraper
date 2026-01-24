"""
Indian Startup Scraper - Startup India Website Data Extraction Tool

Scrapes Indian startup data from the official Startup India government portal
(https://www.startupindia.gov.in) for lead generation, market research, and 
business development purposes.

This web scraping tool extracts:
- Indian startup company names and profiles
- Business stages and sectors
- Location data (Indian cities and states)
- Contact information
- Profile URLs from startupindia.gov.in

Perfect for: investors, researchers, business developers, and anyone building
a database of Indian startup leads.

Keywords: Indian startup scraper, Startup India data extraction, Indian startup leads
"""

import time
import json
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pandas as pd


class StartupIndiaScraper:
    def __init__(self, headless=True):
        """Initialize the scraper with Chrome webdriver"""
        self.base_url = "https://www.startupindia.gov.in/content/sih/en/search.html?roles=Startup&page="
        self.startups_data = []
        
        # Setup Chrome options
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        
    def scrape_page(self, page_number):
        """Scrape data from a single page"""
        url = f"{self.base_url}{page_number}"
        print(f"Scraping page {page_number}: {url}")
        
        try:
            self.driver.get(url)
            time.sleep(3)  # Wait for page to load
            
            # Wait for startup listings to load
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/content/sih/en/profile.Startup']")))
            
            # Scroll to load more content
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
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
            # Find all startup links
            startup_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/content/sih/en/profile.Startup']")
            
            print(f"Found {len(startup_links)} startup links on page {page_number}")
            
            for link in startup_links:
                try:
                    # Get the link text and URL
                    text = link.text.strip()
                    profile_url = link.get_attribute('href')
                    
                    if not text or not profile_url:
                        continue
                    
                    # Parse the text to extract details
                    # Format: "COMPANY NAME Stage Location Sector"
                    parts = text.split('\n')
                    
                    startup_data = {
                        'profile_url': profile_url,
                        'raw_text': text,
                        'company_name': '',
                        'stage': '',
                        'location': '',
                        'sector': '',
                        'scraped_at': datetime.now().isoformat(),
                        'page_number': page_number
                    }
                    
                    # Try to parse the text
                    if len(parts) >= 1:
                        startup_data['company_name'] = parts[0].strip()
                    if len(parts) >= 2:
                        # Second line usually contains stage and location
                        second_line = parts[1].strip()
                        # Try to identify stage keywords
                        stages = ['Ideation', 'Validation', 'Early Traction', 'Scaling']
                        for stage in stages:
                            if stage in second_line:
                                startup_data['stage'] = stage
                                # Rest is location
                                startup_data['location'] = second_line.replace(stage, '').strip()
                                break
                    if len(parts) >= 3:
                        startup_data['sector'] = parts[2].strip()
                    
                    # If parsing failed, try alternative approach
                    if not startup_data['stage'] or not startup_data['location']:
                        # Use original text and let user process it
                        words = text.split()
                        startup_data['company_name'] = ' '.join(words[:3]) if len(words) >= 3 else text
                    
                    self.startups_data.append(startup_data)
                    
                except Exception as e:
                    print(f"Error parsing startup link: {e}")
                    continue
            
            return len(startup_links)
            
        except TimeoutException:
            print(f"Timeout loading page {page_number}")
            return 0
        except Exception as e:
            print(f"Error scraping page {page_number}: {e}")
            return 0
    
    def scrape_multiple_pages(self, start_page=1, end_page=10):
        """Scrape multiple pages"""
        print(f"Starting scraping from page {start_page} to {end_page}")
        
        for page in range(start_page, end_page + 1):
            count = self.scrape_page(page)
            if count == 0:
                print(f"No startups found on page {page}. Stopping.")
                break
            print(f"Collected {len(self.startups_data)} startups so far")
            time.sleep(2)  # Be respectful to the server
        
        print(f"\nTotal startups collected: {len(self.startups_data)}")
        return self.startups_data
    
    def scrape_startup_details(self, profile_url):
        """Scrape detailed information from a startup's profile page"""
        try:
            self.driver.get(profile_url)
            time.sleep(2)
            
            details = {
                'website': '',
                'email': '',
                'phone': '',
                'description': '',
                'founders': '',
                'founded_year': '',
                'team_size': ''
            }
            
            # Try to find common elements
            try:
                # Look for website links
                website_elem = self.driver.find_element(By.CSS_SELECTOR, "a[href*='http']")
                details['website'] = website_elem.get_attribute('href')
            except:
                pass
            
            try:
                # Look for description
                desc_elem = self.driver.find_element(By.CSS_SELECTOR, ".description, .about, .overview")
                details['description'] = desc_elem.text.strip()
            except:
                pass
            
            return details
            
        except Exception as e:
            print(f"Error scraping profile details: {e}")
            return {}
    
    def save_to_csv(self, filename='startup_leads.csv'):
        """Save scraped data to CSV file"""
        if not self.startups_data:
            print("No data to save")
            return
        
        df = pd.DataFrame(self.startups_data)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Data saved to {filename}")
        return filename
    
    def save_to_excel(self, filename='startup_leads.xlsx'):
        """Save scraped data to Excel file"""
        if not self.startups_data:
            print("No data to save")
            return
        
        df = pd.DataFrame(self.startups_data)
        df.to_excel(filename, index=False, engine='openpyxl')
        print(f"Data saved to {filename}")
        return filename
    
    def save_to_json(self, filename='startup_leads.json'):
        """Save scraped data to JSON file"""
        if not self.startups_data:
            print("No data to save")
            return
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.startups_data, f, indent=2, ensure_ascii=False)
        print(f"Data saved to {filename}")
        return filename
    
    def get_summary(self):
        """Get summary statistics of scraped data"""
        if not self.startups_data:
            return "No data collected"
        
        df = pd.DataFrame(self.startups_data)
        
        summary = {
            'total_startups': len(df),
            'unique_sectors': df['sector'].nunique() if 'sector' in df.columns else 0,
            'unique_locations': df['location'].nunique() if 'location' in df.columns else 0,
            'by_stage': df['stage'].value_counts().to_dict() if 'stage' in df.columns else {},
            'top_sectors': df['sector'].value_counts().head(10).to_dict() if 'sector' in df.columns else {},
            'top_locations': df['location'].value_counts().head(10).to_dict() if 'location' in df.columns else {}
        }
        
        return summary
    
    def close(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            print("Browser closed")


def main():
    """Main execution function"""
    print("=" * 60)
    print("Startup India Lead Generation Scraper")
    print("=" * 60)
    
    # Initialize scraper
    scraper = StartupIndiaScraper(headless=False)  # Set to True for headless mode
    
    try:
        # Scrape pages (adjust range as needed)
        start_page = 1
        end_page = 5  # Start with 5 pages, adjust as needed
        
        print(f"\nScraping pages {start_page} to {end_page}...")
        scraper.scrape_multiple_pages(start_page, end_page)
        
        # Display summary
        print("\n" + "=" * 60)
        print("SCRAPING SUMMARY")
        print("=" * 60)
        summary = scraper.get_summary()
        print(json.dumps(summary, indent=2))
        
        # Save data in multiple formats
        print("\n" + "=" * 60)
        print("SAVING DATA")
        print("=" * 60)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        scraper.save_to_csv(f'startup_leads_{timestamp}.csv')
        scraper.save_to_excel(f'startup_leads_{timestamp}.xlsx')
        scraper.save_to_json(f'startup_leads_{timestamp}.json')
        
        print("\n" + "=" * 60)
        print("SCRAPING COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError during scraping: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Always close the browser
        scraper.close()


if __name__ == "__main__":
    main()
