@echo off
echo ============================================
echo Startup India Lead Generation Scraper
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python is installed.
echo.

REM Check if requirements are installed
echo Checking dependencies...
python -c "import selenium, pandas, openpyxl" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo Dependencies installed successfully!
) else (
    echo All dependencies are installed.
)

echo.
echo ============================================
echo Starting Interactive Menu...
echo ============================================
echo.

REM Run the main script
python run.py

pause
