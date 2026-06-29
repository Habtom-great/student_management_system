from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY
SECRET_KEY = 'django-insecure-change-this'
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = "habtoma321@gmail.com"
EMAIL_HOST_PASSWORD = "Jesusisking@3217"

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# APPLICATIONS
INSTALLED_APPS = [
   # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party Apps
      "django_extensions",
    # Local Apps
    "apps.accounts",
    "apps.dashboard",
    "apps.students",
    "apps.instructors",
    "apps.departments",
    "apps.programs",
    "apps.courses",
    "apps.assignments",
    "apps.quizzes",
    "apps.exams",
    "apps.attendance",
    "apps.grades",
    "apps.progress",
    "apps.certificates",
    "apps.forum",
    "apps.messaging",
    "apps.notifications",
    "apps.analytics",
    "apps.reports",
    "apps.payments",
    "apps.settings",
    "apps.api",
]
AUTHENTICATION_BACKENDS = [
    "apps.accounts.backends.EmailBackend",
    "django.contrib.auth.backends.ModelBackend",
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    
]


# URL CONFIG
ROOT_URLCONF = 'config.urls'


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# AUTH MODEL (IMPORTANT FIX)
AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/accounts/login/"


# STATIC FILES
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# TIMEZONE
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True