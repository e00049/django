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
