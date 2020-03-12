from environs import Env

env = Env()
env.read_env()

# Database
# https://docs.djangoproject_name.com/en/stable/ref/settings/#databases
#
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # NOQA Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': env.str('DB_NAME', default='nekochat'),
        'USER': env.str('DB_USER', default='nekochat'),
        'PASSWORD': env.str('DB_PASSWORD', default='nekochat'),
        'HOST': env.str('DB_HOST', default='127.0.0.1'),
        'PORT': env.str('DB_PORT', default='5432'),
    }
}
