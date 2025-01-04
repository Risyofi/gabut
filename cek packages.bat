@echo off
echo Checking and installing required Python packages...

REM Daftar package
set packages=jupyter pandas numpy seaborn matplotlib scikit-learn missingno apyori

REM Loop untuk setiap package
for %%p in (%packages%) do (
    echo Checking %%p...
    python -c "import %%p" 2>nul
    if errorlevel 1 (
        echo %%p not installed. Installing...
        python -m pip install %%p
    ) else (
        echo %%p is already installed.
    )
)

echo All packages are checked.
pause
