# Startup India Lead Generation Scraper 🚀

An AI-powered automation tool to scrape startup data from [Startup India](https://www.startupindia.gov.in) for lead generation purposes.

## Features

✅ **Automated Data Collection**
- Scrapes startup listings from multiple pages
- Extracts company name, stage, location, sector, and profile URLs
- Handles pagination automatically

✅ **Multiple Export Formats**
- CSV (Excel-compatible)
- Excel (.xlsx)
- JSON

✅ **Advanced Filtering**
- Filter by stage (Ideation, Validation, Early Traction, Scaling)
- Filter by sector (AI, FinTech, Healthcare, etc.)
- Filter by state/location

✅ **Detailed Profile Scraping** (Optional)
- Extract contact information (email, phone, website)
- Company description and founding details
- Social media links

✅ **Smart Features**
- Duplicate removal
- Rate limiting (respectful scraping)
- Progress tracking
- Comprehensive reporting
- Headless browser support

## Installation

### Prerequisites
- Python 3.8 or higher
- Chrome browser installed
- ChromeDriver (automatically managed)

### Setup

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Verify installation**:
```bash
python startup_scraper.py --help
```

## Usage

### Basic Scraping

Run the basic scraper (5 pages by default):
```bash
python startup_scraper.py
```

### Advanced Scraping with Configuration

1. **Edit `config.py`** to customize settings:
```python
START_PAGE = 1
END_PAGE = 20  # Scrape 20 pages

HEADLESS_MODE = True  # Run without opening browser window

# Filter options
FILTER_BY_STAGE = ['Scaling', 'Early Traction']
FILTER_BY_SECTOR = ['AI', 'FinTech', 'Healthcare']
FILTER_BY_STATE = ['Karnataka', 'Maharashtra']

SCRAPE_PROFILE_DETAILS = True  # Enable detailed scraping
```

2. **Run the advanced scraper**:
```bash
python advanced_scraper.py
```

## Output Files

The scraper generates timestamped files:
- `startup_leads_YYYYMMDD_HHMMSS.csv` - CSV format
- `startup_leads_YYYYMMDD_HHMMSS.xlsx` - Excel format
- `startup_leads_YYYYMMDD_HHMMSS.json` - JSON format

### Sample Output Structure

```csv
company_name,stage,city,state,location,sector,profile_url,page_number,scraped_at
"TechStartup Pvt Ltd","Scaling","Bengaluru","Karnataka","Bengaluru, Karnataka","AI","https://...",1,"2026-01-24T..."
```

## Configuration Options

### Scraping Parameters
| Parameter | Description | Default |
|-----------|-------------|---------|
| `START_PAGE` | First page to scrape | 1 |
| `END_PAGE` | Last page to scrape | 10 |
| `HEADLESS_MODE` | Run browser in background | True |
| `WAIT_TIMEOUT` | Element wait timeout (seconds) | 20 |
| `PAGE_LOAD_DELAY` | Delay after page load | 3 |

### Export Options
| Parameter | Description | Default |
|-----------|-------------|---------|
| `EXPORT_CSV` | Export to CSV | True |
| `EXPORT_EXCEL` | Export to Excel | True |
| `EXPORT_JSON` | Export to JSON | True |

### Filters
| Parameter | Description | Example |
|-----------|-------------|---------|
| `FILTER_BY_STAGE` | Filter by startup stage | `['Scaling']` |
| `FILTER_BY_SECTOR` | Filter by industry sector | `['AI', 'FinTech']` |
| `FILTER_BY_STATE` | Filter by state | `['Karnataka']` |

## Data Fields

### Basic Information
- `company_name` - Startup company name
- `stage` - Business stage (Ideation, Validation, Early Traction, Scaling)
- `location` - Full location string
- `city` - City name
- `state` - State/UT name
- `sector` - Industry sector
- `profile_url` - Link to startup profile
- `page_number` - Page where found
- `scraped_at` - Timestamp

### Detailed Information (when enabled)
- `email` - Contact email
- `phone` - Contact phone
- `website` - Company website
- `description` - Company description
- `founded_year` - Year founded
- `team_size` - Number of employees

## Best Practices

1. **Start Small**: Test with 2-3 pages first
2. **Respect Rate Limits**: Don't scrape too aggressively
3. **Check Robots.txt**: Ensure compliance with website policies
4. **Use Headless Mode**: For production runs
5. **Regular Backups**: Save scraped data regularly

## Troubleshooting

### Common Issues

**Issue**: ChromeDriver error
```bash
# Solution: Update selenium and webdriver-manager
pip install --upgrade selenium webdriver-manager
```

**Issue**: Timeout errors
```python
# Solution: Increase timeout in config.py
WAIT_TIMEOUT = 30
PAGE_LOAD_DELAY = 5
```

**Issue**: No data collected
- Check your internet connection
- Verify the website is accessible
- Try with `HEADLESS_MODE = False` to see what's happening

**Issue**: Incomplete data
- Some fields may be empty if not present on the page
- Enable detailed profile scraping for more information

## Advanced Usage

### Custom Scraping Script

```python
from advanced_scraper import AdvancedStartupScraper
import config

# Override config
config.START_PAGE = 1
config.END_PAGE = 50
config.FILTER_BY_SECTOR = ['AI', 'Machine Learning']

# Initialize and run
scraper = AdvancedStartupScraper(headless=True)
try:
    scraper.scrape_all()
    scraper.save_data()
    scraper.generate_report()
finally:
    scraper.close()
```

### Data Analysis

```python
import pandas as pd

# Load scraped data
df = pd.read_csv('startup_leads_20260124_120000.csv')

# Analyze by sector
print(df['sector'].value_counts())

# Filter AI startups in Karnataka
ai_startups = df[(df['sector'].str.contains('AI', na=False)) & 
                 (df['state'] == 'Karnataka')]

# Export filtered data
ai_startups.to_excel('ai_startups_karnataka.xlsx', index=False)
```

## Lead Generation Use Cases

1. **Investor Research**: Find startups by stage and sector
2. **Partnership Opportunities**: Identify companies in specific locations
3. **Market Analysis**: Analyze startup ecosystem trends
4. **Sales Prospecting**: Build targeted lead lists
5. **Competition Research**: Track companies in your sector

## Data Privacy & Ethics

⚠️ **Important Notes**:
- This tool is for research and business development purposes
- Respect data privacy and website terms of service
- Don't use scraped data for spam or unsolicited marketing
- Always verify and enrich data through official channels
- Follow GDPR and local data protection laws

## Performance

- **Speed**: ~20-30 startups per page
- **Time**: ~5-10 seconds per page
- **Scalability**: Can handle 100+ pages
- **Memory**: Minimal (data stored incrementally)

## Updates & Maintenance

The website structure may change. If scraping fails:
1. Check if the website is accessible
2. Inspect the page structure (press F12 in browser)
3. Update CSS selectors in the scraper code
4. Report issues or contribute fixes

## Contributing

Contributions are welcome! Areas for improvement:
- Better data parsing algorithms
- Additional export formats
- Email enrichment integration
- CRM integration (Salesforce, HubSpot)
- Proxy support for large-scale scraping

## License

This tool is provided as-is for educational and business purposes. Users are responsible for compliance with applicable laws and website terms of service.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the configuration options
3. Test with a small dataset first
4. Ensure all dependencies are installed

## Roadmap

- [ ] API integration for real-time data
- [ ] Email verification and enrichment
- [ ] LinkedIn profile matching
- [ ] CRM export integration
- [ ] Scheduled automated scraping
- [ ] Web dashboard for monitoring
- [ ] Machine learning for data classification

---

**Happy Lead Hunting! 🎯**

Made with ❤️ for the startup ecosystem
