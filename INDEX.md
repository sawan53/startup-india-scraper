# 🎯 Startup India Lead Generation Scraper

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.16-green)
![Status](https://img.shields.io/badge/Status-Ready-success)

An automated web scraper to collect startup data from [Startup India](https://www.startupindia.gov.in) for lead generation, market research, and investor prospecting.

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Python
Download from [python.org](https://www.python.org/downloads/) (3.8 or higher)

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run
**Windows**: Double-click `start.bat` or `quick_start.bat`

**Mac/Linux**:
```bash
python run.py
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **Automated Scraping** | Scrapes multiple pages automatically |
| 🎯 **Smart Filtering** | Filter by stage, sector, location |
| 📊 **Multiple Exports** | CSV, Excel, JSON formats |
| 🔍 **Data Enrichment** | Add insights and categorization |
| ⚡ **Fast & Efficient** | 20-30 startups per page |
| 🎨 **User Friendly** | Interactive menu interface |

---

## 📦 What You Get

After scraping, you'll receive:

```
✓ startup_leads_TIMESTAMP.csv   (Excel-compatible)
✓ startup_leads_TIMESTAMP.xlsx  (Excel format)
✓ startup_leads_TIMESTAMP.json  (JSON format)
```

### Data Fields:
- Company Name
- Business Stage (Ideation → Validation → Early Traction → Scaling)
- Location (City, State)
- Industry Sector
- Profile URL
- And more...

---

## 🎮 Usage Options

### Option 1: Windows Batch Files (Easiest)
```bash
start.bat          # Interactive menu
quick_start.bat    # Quick scrape (5 pages)
```

### Option 2: Python Scripts
```bash
python run.py                # Interactive menu
python startup_scraper.py    # Basic scraper
python advanced_scraper.py   # Advanced with filters
```

### Option 3: Custom Code
```python
from startup_scraper import StartupIndiaScraper

scraper = StartupIndiaScraper(headless=True)
scraper.scrape_multiple_pages(1, 10)
scraper.save_to_excel('my_leads.xlsx')
scraper.close()
```

---

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Pages to scrape
START_PAGE = 1
END_PAGE = 10    # ~200 startups

# Filters
FILTER_BY_STAGE = ['Scaling', 'Early Traction']
FILTER_BY_SECTOR = ['AI', 'FinTech', 'Healthcare']
FILTER_BY_STATE = ['Karnataka', 'Maharashtra']

# Options
HEADLESS_MODE = True
SCRAPE_PROFILE_DETAILS = False
```

---

## 🎯 Use Cases

### 1️⃣ Investor Research
Find investment-ready startups:
```python
FILTER_BY_STAGE = ['Scaling', 'Early Traction']
FILTER_BY_SECTOR = ['AI', 'FinTech']
```

### 2️⃣ Market Analysis
Analyze startup ecosystem:
```python
END_PAGE = 50  # More data
EXPORT_EXCEL = True
```

### 3️⃣ Sales Prospecting
B2B lead generation:
```python
FILTER_BY_STATE = ['Karnataka', 'Maharashtra', 'Delhi']
SCRAPE_PROFILE_DETAILS = True
```

### 4️⃣ Partnership Discovery
Find potential partners:
```python
FILTER_BY_SECTOR = ['Healthcare', 'HealthTech']
FILTER_BY_STAGE = ['Scaling']
```

---

## 📊 Example Output

```csv
company_name,stage,city,state,sector,profile_url
"TechVenture Pvt Ltd","Scaling","Bengaluru","Karnataka","AI","https://..."
"HealthCare Innovations","Early Traction","Mumbai","Maharashtra","Healthcare","https://..."
"FinTech Solutions Ltd","Scaling","Gurugram","Haryana","FinTech","https://..."
```

---

## 🔧 Advanced Features

### Data Enrichment
Add insights to your leads:
```bash
python data_enrichment.py startup_leads.csv enriched_output.csv
```

Adds:
- Maturity level (1-4 scale)
- Investment readiness
- City tier classification
- Risk level assessment
- Broad category grouping

### Custom Filtering
Post-scraping analysis:
```python
import pandas as pd

df = pd.read_csv('startup_leads.csv')

# Find AI startups in Tier 1 cities
ai_startups = df[
    (df['sector'].str.contains('AI')) &
    (df['city'].isin(['Bengaluru', 'Mumbai', 'Delhi']))
]

ai_startups.to_excel('ai_tier1_leads.xlsx')
```

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [README.md](README.md) | Complete documentation |
| [QUICKSTART.md](QUICKSTART.md) | Quick start guide |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Project overview |
| [examples.py](examples.py) | Code examples |
| [config.py](config.py) | Configuration reference |

---

## 🛠️ Requirements

- Python 3.8 or higher
- Chrome browser
- Internet connection
- Windows/Mac/Linux

### Python Packages:
- selenium
- pandas
- openpyxl
- webdriver-manager

---

## 🚨 Important Notes

### Legal & Ethical
- ✅ For research and business development
- ✅ Respect website terms of service
- ✅ Follow data protection laws (GDPR, etc.)
- ❌ Don't use for spam or harassment
- ❌ Verify data before important decisions

### Best Practices
- Start with 2-3 pages to test
- Use headless mode for production
- Respect rate limits (built-in delays)
- Save data regularly
- Verify critical information

---

## 🐛 Troubleshooting

### Common Issues

**Problem**: Module not found
```bash
Solution: pip install -r requirements.txt
```

**Problem**: ChromeDriver error
```bash
Solution: pip install --upgrade selenium webdriver-manager
```

**Problem**: No data collected
```bash
Solution: 
1. Check internet connection
2. Set HEADLESS_MODE = False in config.py
3. Try fewer pages first (END_PAGE = 2)
```

**Problem**: Slow performance
```python
Solution: In config.py
PAGE_LOAD_DELAY = 5
DELAY_BETWEEN_PAGES = 3
```

---

## 📈 Performance

| Metric | Value |
|--------|-------|
| Speed | 20-30 startups/page |
| Time | 5-10 seconds/page |
| Capacity | 100+ pages |
| Output | 200-300 leads per 10 pages |

---

## 🎓 Learning Path

1. **Beginner**: Use `quick_start.bat` or `python startup_scraper.py`
2. **Intermediate**: Edit `config.py` and use `advanced_scraper.py`
3. **Advanced**: Use `examples.py` and create custom scripts
4. **Expert**: Integrate with CRM, add API enrichment

---

## 🔄 Typical Workflow

```
1. Configure → Edit config.py with filters
2. Scrape → Run advanced_scraper.py
3. Enrich → Run data_enrichment.py
4. Analyze → Open Excel file
5. Export → Import to CRM/sales tool
```

---

## 🌟 Pro Tips

- **Filter Early**: Use filters in config.py to save time
- **Test First**: Always test with 2-3 pages
- **Enrich Data**: Use enrichment module for better insights
- **Regular Runs**: Schedule weekly/monthly scraping
- **Backup Data**: Save scraped data regularly
- **Verify Emails**: Use email verification services
- **LinkedIn Match**: Cross-reference with LinkedIn

---

## 📞 Support & Help

### Getting Help
1. Check [QUICKSTART.md](QUICKSTART.md) troubleshooting
2. Review [examples.py](examples.py) for usage patterns
3. Read [README.md](README.md) for detailed docs
4. Test with small dataset first

### Files Overview
```
📁 Startup-india-scrapper/
├── 🚀 start.bat              # Windows quick launcher
├── ⚡ quick_start.bat        # Quick scrape launcher
├── 🐍 startup_scraper.py     # Basic scraper
├── 🔥 advanced_scraper.py    # Advanced scraper
├── ⚙️ config.py              # Configuration
├── 💎 data_enrichment.py     # Data enrichment
├── 🎯 run.py                 # Interactive menu
├── 📘 examples.py            # Usage examples
├── 📦 requirements.txt       # Dependencies
├── 📖 README.md              # Full documentation
├── 🏁 QUICKSTART.md          # Quick start guide
└── 📋 PROJECT_SUMMARY.md     # Project overview
```

---

## 🎉 Ready to Start?

### Windows Users:
Double-click `start.bat` for interactive menu

### All Users:
```bash
pip install -r requirements.txt
python run.py
```

---

## 📄 License

This tool is provided as-is for educational and business purposes. Users are responsible for compliance with applicable laws and website terms of service.

---

## 🙏 Acknowledgments

Built for the Indian startup ecosystem to facilitate connections, research, and growth.

---

**Happy Lead Hunting! 🚀**

Made with ❤️ for entrepreneurs, investors, and researchers
