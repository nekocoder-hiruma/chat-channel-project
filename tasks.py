from invoke import task


@task
def create_databases(c):
    """
    Create local postgres databases if not created
    """
    # Add citext extension
    c.run('psql -c "CREATE EXTENSION IF NOT EXISTS citext;" -d template1', warn=True)
    # Add local DB and user
    c.run('psql -c "CREATE DATABASE nekochat;"', warn=True)
    c.run('psql -c "CREATE USER nekochat WITH PASSWORD \'nekochat\'"', warn=True)
    c.run('psql -c "GRANT ALL PRIVILEGES ON DATABASE nekochat TO nekochat;"', warn=True)
    # Add test DB user
    c.run('psql -c "CREATE USER chat_test WITH PASSWORD \'chat_test\'"', warn=True)
    c.run('psql -c "ALTER USER nekochat CREATEDB;"', warn=True)


@task
def build(c):
    """
    Run migrations, load fixtures, compile staticfiles
    """
    run_migrations(c)
    dev_static(c)


@task
def initial(c):
    """
    Create databases, create env file, run build step
    """
    create_databases(c)
    create_dotenv(c)
    build(c)


@task
def create_dotenv(c):
    """
    Create env file
    """
    c.run('cp template.env .env')


@task
def dev(c):
    with c.cd('src/meta-api/'):
        c.run('python ./manage.py runserver')


@task
def dev_static(c):
    with c.cd('src/meta-api/static'):
        c.run('npm install')
        c.run('npm run build')


@task
def make_migrations(c):
    with c.cd('src/meta-api/'):
        c.run('python ./manage.py makemigrations --noinput --settings=conf.settings.local')


@task
def run_migrations(c):
    with c.cd('src/meta-api/'):
        c.run('python ./manage.py migrate --noinput --settings=conf.settings.local')
