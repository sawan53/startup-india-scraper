# 🎯 Complete Installation & Testing Guide

## Prerequisites Checklist

Before you begin, ensure you have:
- [ ] Windows 10/11 (or Mac/Linux)
- [ ] Internet connection
- [ ] Google Chrome browser installed
- [ ] Administrator access (for installing Python)

---

## Step-by-Step Installation

### 1️⃣ Install Python (if not already installed)

#### Windows:
1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or higher (Latest version recommended)
3. **IMPORTANT**: During installation, check ✅ "Add Python to PATH"
4. Click "Install Now"
5. Wait for installation to complete

#### Verify Installation:
Open PowerShell or Command Prompt and type:
```powershell
python --version
```
You should see: `Python 3.x.x`

If you see an error, Python is not in your PATH. Reinstall and check the PATH option.

---

### 2️⃣ Download/Navigate to Project Folder

Open PowerShell in the project folder:
```powershell
cd "d:\Personal\Startup-india-scrapper"
```

---

### 3️⃣ Install Dependencies

Run this command:
```powershell
pip install -r requirements.txt
```

**What this installs:**
- `selenium` - Web automation
- `pandas` - Data processing
- `openpyxl` - Excel export
- `webdriver-manager` - Chrome driver management
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `lxml` - XML processing

**Installation should take 1-3 minutes.**

If you see errors, try:
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### 4️⃣ Verify Installation

Test if all packages are installed:
```powershell
python -c "import selenium, pandas, openpyxl; print('All packages installed successfully!')"
```

You should see: `All packages installed successfully!`

---

## Testing the Scraper

### Test 1: Quick Test (Recommended First)

#### Windows:
Double-click `quick_start.bat`

#### Mac/Linux or PowerShell:
```bash
python startup_scraper.py
```

**What happens:**
- Browser opens (or runs in background)
- Scrapes 5 pages (~100-150 startups)
- Takes 1-2 minutes
- Creates 3 files: `.csv`, `.xlsx`, `.json`

**Expected Output:**
```
==============================================================
Startup India Lead Generation Scraper
==============================================================
Scraping pages 1 to 5...
Scraping page 1: https://www.startupindia.gov.in/...
Found 25 startup links on page 1
Collected 25 startups so far
...
Total startups collected: 125
Data saved to startup_leads_20260124_123456.csv
Data saved to startup_leads_20260124_123456.xlsx
Data saved to startup_leads_20260124_123456.json
SCRAPING COMPLETED SUCCESSFULLY!
```

---

### Test 2: Interactive Menu

#### Windows:
Double-click `start.bat`

#### Mac/Linux or PowerShell:
```bash
python run.py
```

**Menu Options:**
```
1. Run basic scraper (recommended for first-time users)
2. Run advanced scraper (with filters and configuration)
3. Install/update requirements
4. View configuration
5. Exit
```

Select `1` for your first test.

---

### Test 3: Advanced Scraper with Filters

1. **Edit configuration:**
   Open `config.py` in any text editor (Notepad, VS Code, etc.)

2. **Customize settings:**
   ```python
   START_PAGE = 1
   END_PAGE = 3  # Start small for testing
   HEADLESS_MODE = False  # See the browser in action
   
   # Add filters
   FILTER_BY_STAGE = ['Scaling']
   FILTER_BY_SECTOR = ['AI']
   ```

3. **Save and run:**
   ```powershell
   python advanced_scraper.py
   ```

---

## Verifying Output

### Check Generated Files

After scraping, you should see files like:
- `startup_leads_20260124_123456.csv`
- `startup_leads_20260124_123456.xlsx`
- `startup_leads_20260124_123456.json`

### Open in Excel

1. Double-click the `.xlsx` file
2. You should see columns:
   - company_name
   - stage
   - city
   - state
   - location
   - sector
   - profile_url
   - page_number
   - scraped_at

### Sample Data Check

Verify you see data like:
```
Company Name: TARAVIHANSHI ENTERPRISES
Stage: Ideation
City: Medchal Malkajgiri
State: Telangana
Sector: Professional & Commercial Services
```

---

## Test Data Enrichment

Once you have scraped data:

```powershell
python data_enrichment.py startup_leads_20260124_123456.csv output_enriched.csv
```

**What it adds:**
- Maturity level
- Investment readiness
- Risk level
- City tier classification
- Broad category grouping

Open `output_enriched.csv` to see new columns.

---

## Troubleshooting Common Issues

### Issue 1: "Python is not recognized"
**Solution:**
- Reinstall Python with "Add to PATH" checked
- Or manually add Python to PATH:
  1. Search for "Environment Variables" in Windows
  2. Edit PATH
  3. Add: `C:\Users\YourName\AppData\Local\Programs\Python\Python3xx`

### Issue 2: "pip is not recognized"
**Solution:**
```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Issue 3: ChromeDriver errors
**Solution:**
```powershell
pip install --upgrade selenium webdriver-manager
```
WebDriver Manager will automatically download the correct ChromeDriver.

### Issue 4: "No data collected"
**Possible causes:**
1. **No internet connection** - Check your connection
2. **Website changed** - Website structure may have changed
3. **Too fast** - Increase delays in config.py:
   ```python
   PAGE_LOAD_DELAY = 5
   WAIT_TIMEOUT = 30
   ```

**Debug Mode:**
Set `HEADLESS_MODE = False` in config.py to see what's happening

### Issue 5: Timeout errors
**Solution:**
In `config.py`, increase timeouts:
```python
WAIT_TIMEOUT = 30
PAGE_LOAD_DELAY = 5
DELAY_BETWEEN_PAGES = 3
```

### Issue 6: Permission errors
**Solution:**
- Run PowerShell as Administrator
- Or change output directory in code

### Issue 7: Excel file won't open
**Solution:**
- Make sure Microsoft Excel is installed
- Or open CSV file instead (opens in Excel too)
- Or use LibreOffice/Google Sheets

---

## Performance Testing

### Small Test (2 pages)
```python
# In config.py
START_PAGE = 1
END_PAGE = 2
```
**Expected:** 40-60 startups in 30-60 seconds

### Medium Test (10 pages)
```python
# In config.py
START_PAGE = 1
END_PAGE = 10
```
**Expected:** 200-300 startups in 2-3 minutes

### Large Test (50 pages)
```python
# In config.py
START_PAGE = 1
END_PAGE = 50
```
**Expected:** 1000-1500 startups in 10-15 minutes

---

## Testing Filters

### Test 1: Stage Filter
```python
# In config.py
FILTER_BY_STAGE = ['Scaling', 'Early Traction']
END_PAGE = 10
```
Run and verify output only contains specified stages.

### Test 2: Sector Filter
```python
# In config.py
FILTER_BY_SECTOR = ['AI', 'FinTech']
END_PAGE = 10
```
Run and verify output only contains AI/FinTech startups.

### Test 3: Location Filter
```python
# In config.py
FILTER_BY_STATE = ['Karnataka', 'Maharashtra']
END_PAGE = 10
```
Run and verify output only contains startups from these states.

### Test 4: Combined Filters
```python
# In config.py
FILTER_BY_STAGE = ['Scaling']
FILTER_BY_SECTOR = ['AI']
FILTER_BY_STATE = ['Karnataka']
END_PAGE = 20
```
Run and verify output matches all three criteria.

---

## Success Indicators

✅ **Installation Successful** when:
- Python version shows correctly
- All packages install without errors
- Test import succeeds

✅ **Scraping Successful** when:
- Browser opens/closes without errors
- Console shows "Found X startups on page Y"
- Files are created with data
- Excel file opens and shows data

✅ **Configuration Working** when:
- Filters reduce number of results appropriately
- Output matches filter criteria
- Different page ranges work correctly

---

## Next Steps After Testing

Once everything works:

1. **Configure for Production:**
   ```python
   HEADLESS_MODE = True  # Run in background
   START_PAGE = 1
   END_PAGE = 50  # Scrape more pages
   ```

2. **Add Your Filters:**
   ```python
   FILTER_BY_STAGE = ['Your', 'Target', 'Stages']
   FILTER_BY_SECTOR = ['Your', 'Target', 'Sectors']
   ```

3. **Run Regular Scrapes:**
   - Daily: 10-20 pages
   - Weekly: 50-100 pages
   - Monthly: Full scrape

4. **Enrich and Analyze:**
   ```powershell
   python data_enrichment.py your_file.csv
   ```

5. **Export to CRM:**
   - Use examples in `examples.py`
   - Import CSV to Salesforce/HubSpot/etc.

---

## Getting Help

If you encounter issues not covered here:

1. **Check Documentation:**
   - [README.md](README.md) - Full documentation
   - [QUICKSTART.md](QUICKSTART.md) - Quick reference
   - [examples.py](examples.py) - Code examples

2. **Debug Steps:**
   - Set `HEADLESS_MODE = False`
   - Run with 1-2 pages only
   - Check console output for errors
   - Verify internet connection

3. **Test Components:**
   ```powershell
   # Test Python
   python --version
   
   # Test packages
   python -c "import selenium; print('Selenium OK')"
   python -c "import pandas; print('Pandas OK')"
   
   # Test Chrome
   # Open Chrome and verify it's up to date
   ```

---

## Checklist: Is Everything Working?

Before production use, verify:

- [ ] Python installed and in PATH
- [ ] All dependencies installed
- [ ] Basic scraper works (1-2 pages)
- [ ] CSV file created with data
- [ ] Excel file opens correctly
- [ ] Filters work as expected
- [ ] Enrichment module works
- [ ] Configuration changes take effect
- [ ] Headless mode works
- [ ] No errors in console

---

**🎉 Congratulations!** You're ready to generate leads!

For advanced usage, see [examples.py](examples.py) and [README.md](README.md)
