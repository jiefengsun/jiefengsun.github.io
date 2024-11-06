# -*- coding: utf-8 -*- #
# this is the new site

from datetime import datetime
AUTHOR = 'Jiefeng Sun'
SITEURL = 'http://localhost:8000'
   # 'https://jiefengsun.github.io' #

SITENAME = 'Jiefeng personal website'
# SITETITLE = 'Flex'
SITESUBTITLE = 'Jiefeng Sun, Ph.D.'
SITEDESCRIPTION = 'Robotics and Artificial Muscle'
SUMMARY_MAX_LENGTH = 0

PATH = 'content'
SITELOGO = '/images/jiefeng.jpg' # Very interesting, this should be relative to the output folder. Because this is called by Jinjia2 
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'github'
LOAD_CONTENT_CACHE = False
ROBOTS = 'index, follow'
OUTPUT_PATH = 'output'

# Specify a customized theme, via path relative to the settings file

THEME = './themes/Flex2.4' # this is relative the work directory

# TIMEZONE = 'America/Denver'

# I18N_TEMPLATES_LANG = 'en'
# DEFAULT_LANG = 'en'
# OG_LOCALE = 'en_US'
# LOCALE = 'usa'
TIMEZONE = 'America/Denver'
I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US.UTF-8'



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

DELETE_OUTPUT_DIRECTORY = True

SOCIAL = (
    ('github', 'https://github.com/jiefengsun'),
	('linkedin', 'https://www.linkedin.com/in/jiefeng-sun/'),
	
)

MENUITEMS = (('Blog Posts', '/categories.html'),('Sun Robotics Lab ASU', 'https://sunroboticslab.github.io/'),)


DISPLAY_PAGES_ON_MENU = True
PAGES_SORT_ATTRIBUTE = 'sortorder'

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

#DISQUS_SITENAME = "flex-pelican"
#ADD_THIS_ID = 'ra-55adbb025d4f7e55'

# STATIC_PATHS = ['images','pdfs',] # ,'images/TRO', 
STATIC_PATHS = ['images', 'pdfs']
# INDEX_SAVE_AS = 'pages/about.html'

# CUSTOM_CSS = 'static/custom.css'

USE_LESS = True


PLUGIN_PATHS = ['plugins']
PLUGINS = ['render_math']


ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}

