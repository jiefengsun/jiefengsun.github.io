# -*- coding: utf-8 -*- #
# this is the new site

from datetime import datetime
LOAD_CONTENT_CACHE = False
AUTHOR = 'Jiefeng Sun'
SITEURL =  'http://localhost:8000'   # 'https://jiefengsun.github.io' #
SITENAME = 'Jiefeng personal website'
# SITETITLE = 'Flex'
SITESUBTITLE = 'Jiefeng Sun, PhD student'
SITEDESCRIPTION = 'Robotics and Artificial Muscle'
SUMMARY_MAX_LENGTH = 0

PATH = 'content'
SITELOGO = '/images/jiefeng.jpg'
FAVICON = 'C:/Users/jacksee/Documents/blog/content/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'github'
LOAD_CONTENT_CACHE = False
ROBOTS = 'index, follow'
OUTPUT_PATH = 'output'

# Specify a customized theme, via path relative to the settings file
THEME =  'C:/Users/jacksee/Documents/blog/themes/Flex2.4'

TIMEZONE = 'America/Denver'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'usa'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}
PAGE_EXCLUDES = ['/images/TRO']
ARTICLE_EXCLUDES = ['/images/TRO']
READERS = {'html': None}
FEED_ALL_ATOM =  None #'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None #'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
GOOGLE_ANALYTICS = True

SOCIAL = (
    ('github', 'https://github.com/jiefengsun'),
	('linkedin', 'https://www.linkedin.com/in/jiefeng-sun/'),
	
)

MENUITEMS = (('Blog Posts', '/categories.html'),)


DISPLAY_PAGES_ON_MENU = True
PAGES_SORT_ATTRIBUTE = True

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

#DISQUS_SITENAME = "flex-pelican"
#ADD_THIS_ID = 'ra-55adbb025d4f7e55'

STATIC_PATHS = ['images','pdfs',] # ,'images/TRO', 

# CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

PLUGIN_PATHS = ['C:/ProgramData/Anaconda3/Lib/site-packages/pelican/plugins']
PLUGINS = [ 'render_math']

ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}

