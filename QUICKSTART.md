# Quick Start Guide

## Installation (Windows)

### Step 1: Install Python
1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. During installation, check "Add Python to PATH"
3. Verify installation:
```powershell
python --version
```

### Step 2: Install Chrome Browser
Make sure Google Chrome is installed on your system.

### Step 3: Install Dependencies
Open PowerShell in the project folder and run:
```powershell
pip install -r requirements.txt
```

### Step 4: Run the Scraper

#### Option A: Interactive Menu (Easiest)
```powershell
python run.py
```

#### Option B: Basic Scraper (Quick)
```powershell
python startup_scraper.py
```

#### Option C: Advanced Scraper (Customizable)
1. Edit `config.py` to set your preferences
2. Run:
```powershell
python advanced_scraper.py
```

## What You'll Get

After scraping, you'll have three files:
- `startup_leads_TIMESTAMP.csv` - Open in Excel
- `startup_leads_TIMESTAMP.xlsx` - Excel format
- `startup_leads_TIMESTAMP.json` - JSON format

## Sample Output

```csv
company_name,stage,city,state,sector,profile_url
"TechCorp Pvt Ltd","Scaling","Bengaluru","Karnataka","AI","https://..."
"HealthStart Ltd","Early Traction","Mumbai","Maharashtra","Healthcare","https://..."
```

## Quick Configuration

Edit `config.py`:

```python
START_PAGE = 1      # Start from page 1
END_PAGE = 10       # Scrape 10 pages (~200 startups)
HEADLESS_MODE = True  # Run in background

# Optional: Filter results
FILTER_BY_STAGE = ['Scaling', 'Early Traction']
FILTER_BY_SECTOR = ['AI', 'FinTech']
FILTER_BY_STATE = ['Karnataka', 'Maharashtra']
```

## Common Use Cases

### 1. Get AI Startups in Bangalore
```python
# In config.py
FILTER_BY_SECTOR = ['AI', 'Artificial Intelligence']
FILTER_BY_STATE = ['Karnataka']
```

### 2. Find Investment-Ready Startups
```python
# In config.py
FILTER_BY_STAGE = ['Scaling', 'Early Traction']
END_PAGE = 50  # More pages for better coverage
```

### 3. Enrich Existing Data
```powershell
python data_enrichment.py startup_leads.csv output_enriched.csv
```

## Troubleshooting

### Error: "Module not found"
```powershell
pip install -r requirements.txt
```

### Error: "ChromeDriver not found"
```powershell
pip install --upgrade selenium webdriver-manager
```

### No data collected
- Check internet connection
- Try with `HEADLESS_MODE = False` in config.py
- Reduce `END_PAGE` to 2-3 for testing

### Slow performance
- Reduce number of pages in config.py
- Increase delays in config.py:
  ```python
  PAGE_LOAD_DELAY = 5
  DELAY_BETWEEN_PAGES = 3
  ```

## Next Steps

1. **Analyze Data**: Open CSV in Excel or use pandas
2. **Enrich Data**: Run `data_enrichment.py` for more insights
3. **Export to CRM**: Use examples in `examples.py`
4. **Automate**: Set up Windows Task Scheduler for daily runs

## Support

Check [README.md](README.md) for detailed documentation.

## Quick Tips

- Start with 2-3 pages to test
- Use filters to get targeted leads
- Enable detailed scraping only when needed (it's slower)
- Export to Excel for easy viewing
- Respect rate limits (don't scrape too fast)

Happy lead generation! 🚀
