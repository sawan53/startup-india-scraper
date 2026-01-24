"""
Example usage scripts for the Startup India Scraper
"""

# Example 1: Basic usage
def example_basic():
    """Basic scraping example"""
    from startup_scraper import StartupIndiaScraper
    
    scraper = StartupIndiaScraper(headless=True)
    try:
        # Scrape 5 pages
        scraper.scrape_multiple_pages(start_page=1, end_page=5)
        
        # Save data
        scraper.save_to_csv('my_leads.csv')
        scraper.save_to_excel('my_leads.xlsx')
        
        # Get summary
        summary = scraper.get_summary()
        print(summary)
    finally:
        scraper.close()


# Example 2: Advanced usage with filters
def example_advanced_with_filters():
    """Advanced scraping with custom filters"""
    import config
    from advanced_scraper import AdvancedStartupScraper
    
    # Configure filters
    config.START_PAGE = 1
    config.END_PAGE = 20
    config.FILTER_BY_STAGE = ['Scaling', 'Early Traction']
    config.FILTER_BY_SECTOR = ['AI', 'Machine Learning', 'FinTech']
    config.FILTER_BY_STATE = ['Karnataka', 'Maharashtra', 'Delhi']
    
    scraper = AdvancedStartupScraper(headless=True)
    try:
        scraper.scrape_all()
        scraper.save_data()
        scraper.generate_report()
    finally:
        scraper.close()


# Example 3: Scrape and enrich data
def example_scrape_and_enrich():
    """Scrape data and enrich it"""
    from startup_scraper import StartupIndiaScraper
    from data_enrichment import DataEnricher
    import pandas as pd
    
    # Scrape data
    scraper = StartupIndiaScraper(headless=True)
    try:
        scraper.scrape_multiple_pages(start_page=1, end_page=10)
        filename = scraper.save_to_csv('temp_leads.csv')
    finally:
        scraper.close()
    
    # Enrich data
    df = pd.read_csv(filename)
    enriched_df = DataEnricher.enrich_dataframe(df)
    enriched_df.to_excel('enriched_leads.xlsx', index=False)
    
    print(f"Scraped {len(df)} startups and enriched with {len(enriched_df.columns)} fields")


# Example 4: Target specific sectors
def example_target_sectors():
    """Target specific sectors for lead generation"""
    import config
    from advanced_scraper import AdvancedStartupScraper
    
    # Target AI and Healthcare startups
    config.FILTER_BY_SECTOR = ['AI', 'Artificial Intelligence', 'Healthcare', 'HealthTech']
    config.START_PAGE = 1
    config.END_PAGE = 50  # Scrape more pages for better coverage
    
    scraper = AdvancedStartupScraper(headless=True)
    try:
        scraper.scrape_all()
        scraper.save_data()
        
        # Additional analysis
        import pandas as pd
        df = pd.DataFrame(scraper.startups_data)
        
        print(f"\nFound {len(df)} startups in target sectors")
        print("\nBreakdown by state:")
        print(df['state'].value_counts().head(10))
        
    finally:
        scraper.close()


# Example 5: Scrape specific pages
def example_specific_pages():
    """Scrape specific non-consecutive pages"""
    from startup_scraper import StartupIndiaScraper
    
    scraper = StartupIndiaScraper(headless=True)
    try:
        # Scrape specific pages
        pages_to_scrape = [1, 5, 10, 15, 20]
        
        for page in pages_to_scrape:
            print(f"Scraping page {page}...")
            scraper.scrape_page(page)
        
        scraper.save_to_csv('selected_pages_leads.csv')
        
    finally:
        scraper.close()


# Example 6: Daily automated scraping
def example_daily_automation():
    """Example of daily automated scraping"""
    from datetime import datetime
    from startup_scraper import StartupIndiaScraper
    import time
    
    print(f"Starting daily scraping at {datetime.now()}")
    
    scraper = StartupIndiaScraper(headless=True)
    try:
        # Scrape first 10 pages daily
        scraper.scrape_multiple_pages(start_page=1, end_page=10)
        
        # Save with date stamp
        today = datetime.now().strftime("%Y%m%d")
        scraper.save_to_csv(f'daily_leads_{today}.csv')
        
        print(f"Daily scraping completed at {datetime.now()}")
        
    finally:
        scraper.close()


# Example 7: Export to specific format for CRM
def example_crm_export():
    """Export data in CRM-friendly format"""
    from startup_scraper import StartupIndiaScraper
    import pandas as pd
    
    scraper = StartupIndiaScraper(headless=True)
    try:
        scraper.scrape_multiple_pages(start_page=1, end_page=5)
        
        # Convert to DataFrame
        df = pd.DataFrame(scraper.startups_data)
        
        # Format for CRM (example: Salesforce)
        crm_df = pd.DataFrame({
            'Company Name': df['company_name'],
            'Industry': df['sector'],
            'City': df.get('city', ''),
            'State': df.get('state', ''),
            'Website': df['profile_url'],
            'Lead Source': 'Startup India',
            'Lead Stage': df['stage'],
            'Lead Status': 'New',
            'Rating': df['stage'].map({
                'Scaling': 'Hot',
                'Early Traction': 'Warm',
                'Validation': 'Warm',
                'Ideation': 'Cold'
            })
        })
        
        crm_df.to_csv('crm_leads.csv', index=False)
        print("CRM-ready file created: crm_leads.csv")
        
    finally:
        scraper.close()


# Example 8: Analyze and filter existing data
def example_analyze_existing():
    """Analyze and filter existing scraped data"""
    import pandas as pd
    
    # Load existing data
    df = pd.read_csv('startup_leads.csv')
    
    # Filter for investment-ready startups
    investment_ready = df[df['stage'].isin(['Scaling', 'Early Traction'])]
    
    # Filter for specific locations
    bangalore_startups = investment_ready[
        investment_ready['city'].str.contains('Bengaluru|Bangalore', na=False)
    ]
    
    # Filter for tech startups
    tech_sectors = ['AI', 'SaaS', 'FinTech', 'Cloud']
    tech_startups = bangalore_startups[
        bangalore_startups['sector'].str.contains('|'.join(tech_sectors), na=False)
    ]
    
    print(f"Total startups: {len(df)}")
    print(f"Investment ready: {len(investment_ready)}")
    print(f"In Bangalore: {len(bangalore_startups)}")
    print(f"Tech startups: {len(tech_startups)}")
    
    # Export filtered list
    tech_startups.to_excel('bangalore_tech_leads.xlsx', index=False)


if __name__ == "__main__":
    print("Startup India Scraper - Usage Examples")
    print("=" * 60)
    print("\nAvailable examples:")
    print("1. Basic scraping")
    print("2. Advanced with filters")
    print("3. Scrape and enrich")
    print("4. Target specific sectors")
    print("5. Scrape specific pages")
    print("6. Daily automation")
    print("7. CRM export")
    print("8. Analyze existing data")
    print("\nUncomment the example you want to run in the code")
    
    # Uncomment the example you want to run:
    # example_basic()
    # example_advanced_with_filters()
    # example_scrape_and_enrich()
    # example_target_sectors()
    # example_specific_pages()
    # example_daily_automation()
    # example_crm_export()
    # example_analyze_existing()
