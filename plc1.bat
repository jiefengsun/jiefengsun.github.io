rmdir /s "output"
pelican
copy "output\pages\about.html" "output\index.html" /y
ghp-import output -b master
git push origin master

