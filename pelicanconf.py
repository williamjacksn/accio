import logging
import os

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

ARCHIVES_SAVE_AS = ''
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{urlname}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{urlname}'
AUTHOR = 'Rebecca and William Jackson'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CACHE_CONTENT = True
CACHE_PATH = 'cache'
CATEGORIES_SAVE_AS = ''
CATEGORY_FEED_ATOM = None
CATEGORY_SAVE_AS = ''
CHECK_MODIFIED_METHOD = 'md5'
CONTENT_CACHING_LAYER = 'reader'
DEBUG_LAYOUT = False
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
EXTRA_PATH_METADATA = {
    'extra/googleb417364cc8d4ecab.txt': {'path': 'googleb417364cc8d4ecab.html'},
    'extra/headers.txt': {'path': '_headers'},
    'extra/robots.txt': {'path': 'robots.txt'}
}
FEED_ALL_ATOM = 'feeds/all.atom.xml'
GZIP_CACHE = True
LOAD_CONTENT_CACHE = True
PATH = 'content'
RELATIVE_URLS = False
SITENAME = 'Accio Jacksons!'
SITESUBTITLE = 'An 11-inch holly blog with a phoenix feather core'
STATIC_CHECK_IF_MODIFIED = True
STATIC_PATHS = ['extra']
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
THEME = 'themes/accio'
TIMEZONE = 'America/Chicago'
TRANSLATION_FEED_ATOM = None

context = os.getenv('CONTEXT')
url = os.getenv('URL')
deploy_url = os.getenv('DEPLOY_URL')
deploy_prime_url = os.getenv('DEPLOY_PRIME_URL')

log.info(f'CONTEXT: {context}')
log.info(f'URL: {url}')
log.info(f'DEPLOY_URL: {deploy_url}')
log.info(f'DEPLOY_PRIME_URL {deploy_prime_url}')

if context == 'production':
    FEED_DOMAIN = url
    SITEURL = url
else:
    FEED_DOMAIN = deploy_prime_url
    SITEURL = deploy_prime_url