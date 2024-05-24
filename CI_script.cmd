@echo off
:: Главное меню
:Menu
echo Choose action:
echo 1. Download actual dev-version of app
echo 2. Run app
echo 3. Run Unit-Tests
echo 4. Build app

set /p choice=Enter your chose: 

if "%choice%"=="1" (
    call :LoadDevVersion
) else if "%choice%"=="2" (
    call :RunApplication
) else if "%choice%"=="3" (
    call :RunUnitTests
) else if "%choice%"=="4" (
    call :BuildApplication
) else (
    echo Enter valid answer
)

set /p continue=Would you like to continue? (Y/N): 
if /i "%continue%" neq "Y" goto :eof

goto Menu

:LoadDevVersion
rd /s /q calculator
git clone https://github.com/hydeonz/calculator
goto Menu

:RunApplication
python calculator/calc.py
goto Menu

:RunUnitTests
python calculator/unit_test.py
goto Menu

:BuildApplication
python calculator/setup.py build
goto Menu