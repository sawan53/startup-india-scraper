# Startup India Lead Generation Scraper - Project Summary

## 📋 Project Overview

This is a comprehensive web scraping solution designed to extract startup data from the Startup India website for lead generation purposes. The tool automates the collection of startup information including company names, business stages, locations, sectors, and profile links.

## 🎯 Purpose

- **Lead Generation**: Build targeted lists of Indian startups
- **Market Research**: Analyze startup ecosystem trends
- **Investor Research**: Find investment opportunities
- **Partnership Discovery**: Identify potential partners
- **Sales Prospecting**: Create B2B sales leads

## ⚙️ Technical Stack

- **Language**: Python 3.8+
- **Web Automation**: Selenium WebDriver
- **Data Processing**: Pandas
- **Export Formats**: CSV, Excel (XLSX), JSON
- **Browser**: Chrome/Chromium

## 📁 Project Structure

```
Startup-india-scrapper/
├── startup_scraper.py          # Basic scraper (simple, quick)
├── advanced_scraper.py         # Advanced scraper (filters, detailed)
├── config.py                   # Configuration settings
├── data_enrichment.py          # Data enrichment utilities
├── run.py                      # Interactive menu launcher
├── examples.py                 # Usage examples
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
├── QUICKSTART.md              # Quick start guide
└── .gitignore                 # Git ignore file
```

## 🚀 Key Features

### 1. Basic Scraper (`startup_scraper.py`)
- Simple and fast
- Scrapes multiple pages automatically
- Exports to CSV, Excel, JSON
- Summary statistics
- Perfect for beginners

### 2. Advanced Scraper (`advanced_scraper.py`)
- Configurable filters (stage, sector, location)
- Enhanced data extraction
- Duplicate removal
- Optional detailed profile scraping
- Progress tracking
- Comprehensive reporting

### 3. Data Enrichment (`data_enrichment.py`)
- Company name cleaning
- Stage categorization (maturity level, investment readiness)
- Sector categorization (broad categories)
- Location enrichment (city tier classification)
- Contact validation (email, phone)
- Export enriched data

### 4. Configuration (`config.py`)
- Customizable scraping parameters
- Filter options (stage, sector, state)
- Rate limiting settings
- Export preferences
- Browser options

## 📊 Data Fields Collected

### Basic Fields
- Company Name
- Business Stage (Ideation, Validation, Early Traction, Scaling)
- Location (City, State)
- Industry Sector
- Profile URL
- Page Number
- Scraped Timestamp

### Enriched Fields (optional)
- Maturity Level (1-4)
- Investment Readiness
- Risk Level
- Broad Category
- City Tier (Tier 1, 2, 3+)
- Metro Status
- Contact Information (email, phone, website)

## 🎮 Usage Methods

### Method 1: Interactive Menu
```bash
python run.py
```
- User-friendly menu
- Guided setup
- Configuration viewer
- Requirement installer

### Method 2: Direct Execution
```bash
# Basic scraping
python startup_scraper.py

# Advanced scraping
python advanced_scraper.py
```

### Method 3: Custom Scripts
```python
from startup_scraper import StartupIndiaScraper

scraper = StartupIndiaScraper(headless=True)
scraper.scrape_multiple_pages(1, 10)
scraper.save_to_excel('my_leads.xlsx')
scraper.close()
```

## 🔧 Configuration Options

### Scraping Parameters
- `START_PAGE`: First page to scrape (default: 1)
- `END_PAGE`: Last page to scrape (default: 10)
- `HEADLESS_MODE`: Run browser in background (default: True)
- `WAIT_TIMEOUT`: Element wait timeout in seconds (default: 20)

### Filters
- `FILTER_BY_STAGE`: Filter by business stage
- `FILTER_BY_SECTOR`: Filter by industry sector
- `FILTER_BY_STATE`: Filter by state/location

### Export Options
- `EXPORT_CSV`: Export to CSV (default: True)
- `EXPORT_EXCEL`: Export to Excel (default: True)
- `EXPORT_JSON`: Export to JSON (default: True)

### Rate Limiting
- `PAGE_LOAD_DELAY`: Delay after page load (default: 3s)
- `DELAY_BETWEEN_PAGES`: Delay between pages (default: 2s)
- `SCROLL_DELAY`: Delay after scrolling (default: 2s)

## 📈 Performance Metrics

- **Speed**: ~20-30 startups per page
- **Time**: 5-10 seconds per page
- **Capacity**: Can handle 100+ pages
- **Output**: 200-300 leads per 10 pages

## 🎯 Use Case Examples

### 1. AI Startup Research
```python
FILTER_BY_SECTOR = ['AI', 'Machine Learning', 'Deep Learning']
FILTER_BY_STAGE = ['Scaling', 'Early Traction']
```

### 2. Regional Market Analysis
```python
FILTER_BY_STATE = ['Karnataka', 'Maharashtra', 'Delhi']
END_PAGE = 50
```

### 3. Investment Scouting
```python
FILTER_BY_STAGE = ['Scaling']
SCRAPE_PROFILE_DETAILS = True
```

### 4. FinTech Lead Generation
```python
FILTER_BY_SECTOR = ['FinTech', 'Finance', 'Banking']
FILTER_BY_STATE = ['Karnataka', 'Maharashtra']
```

## 🛡️ Best Practices

1. **Start Small**: Test with 2-3 pages first
2. **Use Filters**: Target specific segments
3. **Respect Rate Limits**: Don't scrape aggressively
4. **Headless Mode**: Use for production runs
5. **Regular Exports**: Save data periodically
6. **Data Validation**: Check for duplicates and missing data
7. **Enrich Data**: Use enrichment module for better insights

## 📦 Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run scraper
python run.py
```

## 🔄 Typical Workflow

1. **Configure** → Edit `config.py` with desired settings
2. **Scrape** → Run `advanced_scraper.py`
3. **Enrich** → Run `data_enrichment.py` on output file
4. **Analyze** → Open Excel file and filter/sort
5. **Export** → Import to CRM or use for outreach

## 📊 Output Example

```csv
company_name,stage,city,state,sector,profile_url,maturity_level,city_tier
"TechVenture Pvt Ltd","Scaling","Bengaluru","Karnataka","AI","https://...",4,"Tier 1"
"HealthCare Solutions","Early Traction","Mumbai","Maharashtra","Healthcare","https://...",3,"Tier 1"
```

## 🚨 Important Notes

- **Legal**: Check website terms of service
- **Ethics**: Use data responsibly
- **Privacy**: Respect data protection laws
- **Rate Limiting**: Be respectful to servers
- **Accuracy**: Verify important data points

## 🎓 Learning Resources

- `README.md` - Complete documentation
- `QUICKSTART.md` - Quick start guide
- `examples.py` - Code examples
- `config.py` - Configuration reference

## 🔮 Future Enhancements

- Email enrichment API integration
- LinkedIn profile matching
- CRM direct export (Salesforce, HubSpot)
- Automated scheduling
- Web dashboard
- Machine learning classification
- Real-time monitoring

## 📞 Support

For issues:
1. Check QUICKSTART.md troubleshooting section
2. Review examples.py for usage patterns
3. Verify all dependencies are installed
4. Test with small dataset first

## ✅ Pre-flight Checklist

Before first run:
- [ ] Python 3.8+ installed
- [ ] Chrome browser installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Config.py reviewed and customized
- [ ] Test with 2-3 pages first
- [ ] Headless mode enabled for production

## 🎉 Quick Start Commands

```bash
# Install everything
pip install -r requirements.txt

# Run interactive menu
python run.py

# Quick scrape (5 pages)
python startup_scraper.py

# Advanced scrape (with your config)
python advanced_scraper.py

# Enrich existing data
python data_enrichment.py startup_leads.csv
```

---

**Ready to generate leads! 🚀**

For detailed instructions, see [README.md](README.md)
For quick start, see [QUICKSTART.md](QUICKSTART.md)
