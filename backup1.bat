pelican content -s pelicanconf.py
copy "output\pages\about.html" "output\index.html" /y
set ChromeDataDir="C:\Users\%USERNAME%\Local Settings\Application Data\Google\Chrome\User Data\Default"
set ChromeCache=%ChromeDataDir%\Cache>nul 2>&1
del /q /s /f "%ChromeCache%\*.*">nul 2>&1 
pelican --listen

