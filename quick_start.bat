@echo off
echo ============================================
echo Quick Start - Basic Scraper
echo ============================================
echo.
echo This will scrape 5 pages (~100-150 startups)
echo Estimated time: 1-2 minutes
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    pause
    exit /b 1
)

echo Starting scraper...
echo.

python startup_scraper.py

echo.
echo ============================================
echo Scraping completed!
echo Check the generated files in this folder.
echo ============================================
pause
