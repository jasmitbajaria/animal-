import os
from pathlib import Path
from dotenv import load_dotenv  # ✅ Load environment variables

# Load environment variables from .env file
load_dotenv()

# 🔹 Base directory (project root)
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 Security settings
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')  # Change in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'  # Default: True for local, False for production
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# 🔹 CSRF Trusted Origins (for production deployment)
CSRF_TRUSTED_ORIGINS = os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS', 'http://127.0.0.1,http://localhost').split(',')

# 🔹 Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ Your custom apps
    'home',  # Your main app

    # ✅ Third-party apps
    'crispy_forms',
    'crispy_bootstrap5',
]

# 🔹 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔹 Root URL configuration
ROOT_URLCONF = 'animal_encyclopedia.urls'

# 🔹 Templates settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ Ensure templates are loaded correctly
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🔹 WSGI application
WSGI_APPLICATION = 'animal_encyclopedia.wsgi.application'

# 🔹 Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Change to PostgreSQL or MySQL in production
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔹 Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🔹 Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🔹 Static and media files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # ✅ Fix path issue
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # ✅ Ensure static files are served correctly in production

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # ✅ Ensures animal images & audio are served correctly

# 🔹 Crispy Forms settings for Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# 🔹 Authentication settings
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'  # ✅ Ensure logout redirects correctly
LOGIN_URL = 'login'

# 🔹 Session storage (Fix corruption issues)
SESSION_ENGINE = "django.contrib.sessions.backends.db"  # ✅ Store sessions in DB
SESSION_COOKIE_AGE = 1209600  # 2 weeks
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep session after browser close

# 🔹 Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
