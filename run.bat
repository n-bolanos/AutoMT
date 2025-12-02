@echo off
REM Activate virtual environment, install requirements, and run the main script
setlocal enabledelayedexpansion

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0

echo ------------------------------------------
echo  Checking virtual environment...
echo ------------------------------------------

REM Check if .venv exists
if not exist "%SCRIPT_DIR%.venv" (
    echo Error: .venv folder not found in %SCRIPT_DIR%
    echo Please create a virtual environment first with: python -m venv .venv
    pause
    exit /b 1
)

REM Activate the virtual environment
call "%SCRIPT_DIR%.venv\Scripts\activate.bat"
if errorlevel 1 (
    echo Error: Failed to activate virtual environment
    pause
    exit /b 1
)

echo ------------------------------------------
echo  Installing requirements...
echo ------------------------------------------
REM Install libraries if requirements.txt exists
if exist "%SCRIPT_DIR%requirements.txt" (
    pip install -r "%SCRIPT_DIR%requirements.txt"
    if errorlevel 1 (
        echo Error installing dependencies from requirements.txt
        pause
        call "%SCRIPT_DIR%.venv\Scripts\deactivate.bat"
        exit /b 1
    )
) else (
    echo No requirements.txt found. Skipping installation.
)
echo ------------------------------------------
echo  Running main.py...
echo ------------------------------------------

REM Run the main script
python "%SCRIPT_DIR%main.py"
if errorlevel 1 (
    echo.
    echo Error occurred while running main.py
    pause
)

REM Deactivate the virtual environment
call "%SCRIPT_DIR%.venv\Scripts\deactivate.bat"

endlocal
