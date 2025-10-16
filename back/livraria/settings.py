
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'media'

SECRET_KEY = 'django-insecure-#8y71#h%-=1il2w*9)v=8!e&ivjpi4c3%z)(%la+@yrfradlti'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api', 
    'rest_framework',
    'rest_framework_simplejwt',
     "corsheaders",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    
]

CORS_ALLOW_ALL_ORIGINS = True


ROOT_URLCONF = 'livraria.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'livraria.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # (opcional) Verifica se a senha é muito parecida com atributos do usuário
    # (ex.: username, nome, e-mail). Evita senhas derivadas dos dados do próprio usuário.
    
    #{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},

    # "A senha é muito curta. Deve conter pelo menos 8 caracteres."
    # Define o tamanho mínimo da senha (ajuste o min_length conforme sua política).
   
    #{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},

    # "Esta senha é muito comum."
    # Compara a senha com uma lista de senhas conhecidas/comuns. Opcionalmente,
    # você pode informar sua própria lista com 'password_list_path'.
    
    #{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
     # opcional: 'OPTIONS': {'password_list_path': '/caminho/para/sua-lista.txt'}
    #},

    # "Esta senha é inteiramente numérica."
    # Reprova senhas compostas apenas por dígitos.
    
    #{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]




# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
