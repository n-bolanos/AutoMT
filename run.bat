@echo off
REM Activate virtual environment and run the main script
setlocal enabledelayedexpansion

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0

REM Check if .venv exists
if not exist "%SCRIPT_DIR%.venv" (
    echo Error: .venv folder not found in %SCRIPT_DIR%
    echo Please create a virtual environment first with: python -m venv .venv
    pause
    exit /b 1
)

REM Activate the virtual environment
call "%SCRIPT_DIR%.venv\Scripts\activate.bat"

REM Check if activation was successful
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

REM Run the main script
python "%SCRIPT_DIR%main.py"

REM Keep the window open if there was an error
if errorlevel 1 (
    echo.
    echo Error occurred while running the script
    pause
)

REM Deactivate the virtual environment
deactivate

endlocal
