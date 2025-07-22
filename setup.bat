@echo off
:: Check if the folder name argument is provided
if "%1"=="" (
    echo You must provide a folder name as an argument.
    echo Usage: ./setup.bat {foldername}
    exit /b
)

set foldername=%1

:: Create folder
mkdir "%foldername%"

:: Create the Python file and write initial code
echo. >> "%foldername%\solution.py"
echo. >> "%foldername%\solution.py"
echo sol = Solution() >> "%foldername%\solution.py"