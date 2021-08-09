pelican content -s pelicanconf1.py
copy "output\pages\about.html" "output\index.html" /y
ghp-import output -b master
git push origin master

