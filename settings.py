INSTALLED_APPS = [
    ...
    # Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    'modelcluster',
    'taggit',
    ...
    'a_blog',
]

MIDDLEWARE = [
    ...
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

WAGTAIL_SITE_NAME = 'Blog'
WAGTAILADMIN_BASE_URL = 'http://mywebsite.com'
