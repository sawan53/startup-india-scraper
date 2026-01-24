"""
Quick start script for Startup India Scraper
"""

import sys
import subprocess

def check_requirements():
    """Check if required packages are installed"""
    print("Checking requirements...")
    try:
        import selenium
        import pandas
        import openpyxl
        print("✓ All requirements are installed")
        return True
    except ImportError as e:
        print(f"✗ Missing package: {e.name}")
        print("\nPlease install requirements:")
        print("  pip install -r requirements.txt")
        return False

def run_basic_scraper():
    """Run the basic scraper"""
    print("\n" + "="*70)
    print("STARTING BASIC SCRAPER")
    print("="*70)
    print("This will scrape 5 pages (approximately 100-150 startups)")
    print("Estimated time: 1-2 minutes")
    print("="*70)
    
    response = input("\nContinue? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled")
        return
    
    try:
        import startup_scraper
        startup_scraper.main()
    except Exception as e:
        print(f"Error: {e}")
        print("\nTry running directly: python startup_scraper.py")

def run_advanced_scraper():
    """Run the advanced scraper"""
    print("\n" + "="*70)
    print("STARTING ADVANCED SCRAPER")
    print("="*70)
    print("This will scrape pages according to config.py settings")
    print("You can edit config.py to customize filters and options")
    print("="*70)
    
    response = input("\nContinue? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled")
        return
    
    try:
        import advanced_scraper
        advanced_scraper.main()
    except Exception as e:
        print(f"Error: {e}")
        print("\nTry running directly: python advanced_scraper.py")

def main_menu():
    """Display main menu"""
    print("\n" + "="*70)
    print("STARTUP INDIA LEAD GENERATION SCRAPER")
    print("="*70)
    print("\nOptions:")
    print("1. Run basic scraper (recommended for first-time users)")
    print("2. Run advanced scraper (with filters and configuration)")
    print("3. Install/update requirements")
    print("4. View configuration")
    print("5. Exit")
    print("="*70)
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        if check_requirements():
            run_basic_scraper()
    elif choice == '2':
        if check_requirements():
            run_advanced_scraper()
    elif choice == '3':
        print("\nInstalling requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    elif choice == '4':
        try:
            import config
            print("\nCurrent Configuration:")
            print(f"  Start Page: {config.START_PAGE}")
            print(f"  End Page: {config.END_PAGE}")
            print(f"  Headless Mode: {config.HEADLESS_MODE}")
            print(f"  Scrape Detailed Profiles: {config.SCRAPE_PROFILE_DETAILS}")
            print(f"  Filter by Stage: {config.FILTER_BY_STAGE or 'None'}")
            print(f"  Filter by Sector: {config.FILTER_BY_SECTOR or 'None'}")
            print(f"  Filter by State: {config.FILTER_BY_STATE or 'None'}")
            print("\nEdit config.py to change these settings")
        except Exception as e:
            print(f"Error loading config: {e}")
    elif choice == '5':
        print("\nGoodbye!")
        sys.exit(0)
    else:
        print("\nInvalid choice")
    
    # Return to menu
    input("\nPress Enter to continue...")
    main_menu()

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
        sys.exit(0)
