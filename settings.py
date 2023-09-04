DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': os.environ.get('DB_HOST1'),   
        'PORT': os.environ.get('DB_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

AUTH_USER_MODEL = 'myapp.User'

sudo mysql -u root -p

CREATE DATABASE myproject;
CREATE USER 'e00049'@'%' IDENTIFIED BY 'Google@123!!';
GRANT ALL PRIVILEGES ON *.* TO 'e00049'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;

# 
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_PASSWD = os.environ.get('REDIS_PASSWD')
REDIS_DB = 1

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}",
        "OPTIONS": {
             "PASSWORD": f"{REDIS_PASSWD}",    
             "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
