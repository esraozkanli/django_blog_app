#Projeyle ilgili dosya değşiklikleri buradan yapılır.
"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 3.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wueb*d_iuw)v(@t8y1lzbin7z)2xvr!f4@feikp%pa*i772%)3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #Kendimiz sitemizi tasarladığımızda burayı False yapmamız lazım.

ALLOWED_HOSTS = []


# Application definition

#Djangonun kendi içindeki hazır uygulamalarıdır. Kendimiz yazdığımız(Oluşturuduğumuz) uygulamaları da buraya eklemeiz gerekir. Bu uygulamalar kendi içinde tablo yapıları olabilir. 
INSTALLED_APPS = [
    'django.contrib.admin', #Yönetici panelini oluşturur.
    'django.contrib.auth', #Bir kimlik doğrulama sistemi.
    'django.contrib.contenttypes', #İçerik türleri için bir framework.
    'django.contrib.sessions', #Bir oturum frameworku
    'django.contrib.messages', #Bir mesajlaşma frameworku
    'django.contrib.staticfiles', #Statik dosyaları yönetmek için bir framework.
    "user", #Oluşturduğumuz user uygulamızı tanıttık.
    "article", #Oluşturuduğumuz article uygulamamızı tanıttık.
    'crispy_forms',#Bootstrapleri formlarımıza dahil edebilmek için 'crispy_forms' uygulamamızı dahil etiik.
    'crispy_bootstrap4',#Bootstrapleri formlarımıza dahil edebilmek için 'crispy_bootstrap4' uygulamamızı dahil etiik.
    'ckeditor',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"], #Templates(şablonlar) ları koyacağımız klasörün ismini belirttik.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'tr' #Sitenin dilinin ayarlanma yeri

TIME_ZONE = 'Europe/Istanbul' #Saat bilgisinin nereden alınacağını gösterir.

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"), #BASE_DIR, blog klasörünün bulunduğu yeri gösterir. Yanına static eklediğimizde de blog klasörünün altındaki static klasörüne bak demek istemiş oluyoruz.
]

STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'Bootstrap4'

CKEDITOR_CONFIGS = { #code snippetta hata vermemesi için gerekli düzenlemeleri yaptık.
    "default": {
        "removePlugins": "stylesheetparser",
        "allowedContent" :True,
        "width" :"100%" #CKEditor alanının genişliğini formumuzun alanı kadar ayarladık.
    }
}


#Dosyalarımızın kayıt edileceği klasörü oluşturduk.
MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')