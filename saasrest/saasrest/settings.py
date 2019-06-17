"""
Django settings for saasrest project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from .local_settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER
from .local_settings import STRIPE_LIVE_MODE, STRIPE_LIVE_PUBLIC_KEY, STRIPE_LIVE_SECRET_KEY, \
    STRIPE_TEST_PUBLIC_KEY, STRIPE_TEST_SECRET_KEY, STRIPE_WEBHOOK_ENDPOINT_SECRET
from .local_settings import FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
from .local_settings import SOCIAL_AUTH_GOOGLE_OAUTH2_KEY, SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
from .local_settings import MEMCACHED_LOCATION
from .local_settings import DB_CONFIG
from .local_settings import REDIS_HOSTS
from .local_settings import CELERY_BROKER_URL
from .local_settings import SECRET_KEY
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['192.168.1.22', 'localhost', '127.0.0.1', "*"]

# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB 104857600
# 250MB - 214958080
# 500MB - 429916160
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'sslserver',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # api
    'rest_framework',
    'rest_framework.authtoken',
    'saas_core',
    'authentication',
    'categories',
    'locations',
    'feedback',
    'messaging',
    'notifications',
    'payments',
    'public_configs',
    'services',
    'tags',
    'votes',
    'feed',
    # 'api',
    # auth
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.twitter',
    # tasks
    'celery',
    'colorfield',
    'djmoney',
    'import_export',
    # realtime
    'channels',
    # email templates
    'mjml',
    'debug_toolbar',
    'django_filters',
]

# CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = 'Europe/Sofia'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_AUTHENTICATION_METHOD = 'email'


ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

SOCIAL_AUTH_FORCE_EMAIL_VALIDATION = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_CONFIRM_EMAIL_ON_GET=True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL="https://google.com/"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL="https://facebook.com/"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_EMAIL_FIELD = 'email'
ACCOUNT_LOGOUT_ON_GET = True

AUTH_USER_MODEL = 'authentication.User'

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "authentication.serializers.CustomUserDetailsSerializer",
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "authentication.serializers.CustomRegisterSerializer",
}
SITE_ID = 1

ACCOUNT_ADAPTER = 'authentication.adapters.CustomUserAccountAdapter'

MIDDLEWARE = [
    # cache
    # 'django.middleware.cache.UpdateCacheMiddleware',
    #
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # session
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    # for admin panel reasons
    'django.contrib.messages.middleware.MessageMiddleware',
    # clickjacking
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # //
    # debug
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # cache
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

INTERNAL_IPS = ['192.168.1.22', 'localhost', '127.0.0.1', "*"]


def show_toolbar(request):
    if request.is_ajax():
        return False
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'saasrest.settings.show_toolbar',
}

DEBUG_TOOLBAR_PANELS = [
    'ddt_request_history.panels.request_history.RequestHistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

# TODO: check cookie age
SESSION_COOKIE_AGE = 1209600
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = (
#     'localhost:3000',
# )
# CORS_ORIGIN_REGEX_WHITELIST = (
#     'localhost:3000',
# )

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}
ROOT_URLCONF = 'saasrest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['', os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'templates', 'allauth')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # OAuth
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'saasrest.wsgi.application'
ASGI_APPLICATION = 'saas_core.routing.application'


CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": REDIS_HOSTS,
        },
    },
}
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_CONFIG['NAME'],
        'USER': DB_CONFIG['USER'],
        'PASSWORD': DB_CONFIG['PASSWORD'],
        'HOST': DB_CONFIG['HOST'],
        'PORT': DB_CONFIG['PORT']
    }
}

# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': MEMCACHED_LOCATION,
    }
}

# Key in `CACHES` dict
CACHE_MIDDLEWARE_ALIAS = 'default'

# Additional prefix for cache keys
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# Cache key TTL in seconds
CACHE_MIDDLEWARE_SECONDS = 600


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# use Accept-Language Header (i.e. 'ru-ru', 'es-es', 'en-US', 'bg')
LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'Europe/Sofia'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/saas_api/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = '/saas_api/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 60 * 60 * 24 * 180,  # 15552000 # 180 days
    # 'OAUTH_SINGLE_ACCESS_TOKEN': True,
    'OAUTH_DELETE_EXPIRED': True
}

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticatedOrReadOnly',),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'oauth2_provider.ext.rest_framework.OAuth2Authentication',  # django-oauth-toolkit < 1.0.0
        # django-oauth-toolkit >= 1.0.0
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ),
    # 'rest_framework.pagination.LimitOffsetPagination',
    'DEFAULT_PAGINATION_CLASS': 'saas_core.paginations.MyPagination',
    'PAGINATE_BY': 10,                 # Default to 10
    # Allow client to override, using `?page_size=xxx`.
    'PAGINATE_BY_PARAM': 'page_size',
    # Maximum limit allowed when using `?page_size=xxx`
    'MAX_PAGINATE_BY': 100,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DATETIME_FORMAT': "%Y-%m-%dT%H:%M:%S%z",
    'DATETIME_INPUT_FORMATS': ["%Y-%m-%dT%H:%M:%S%z"]
}


AUTHENTICATION_BACKENDS = (

    # Others auth providers (e.g. Google, OpenId, etc)

    # Google OAuth2
    'social.backends.google.GoogleOAuth2',

    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    # Django
    'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_GOOGLE_PROFILE_EXTRA_PARAMS = {
    'fields': 'email,name,first_name,last_name'
}

# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = FACEBOOK_APP_ID
SOCIAL_AUTH_FACEBOOK_SECRET = FACEBOOK_APP_SECRET

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook.
# Email is not sent by default, to get it, you must request the email permission:
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, first_name, last_name'
}


# Stripe


# Email sending
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
