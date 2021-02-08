# TST: Intro to Django

## Setup VirtualEnv
Create:
```bash
virtualenv --python=python3.9 venv
```
Activate:
```bash
macOS:
source venv/bin/activate

Windows:
./venv/scripts/activate
```
Install requirements:
```bash
pip install -r requirements.txt
```

## Running Migrations
```bash
python manage.py migrate
```

## Create SuperUser
```bash
python manage.py createsuperuser
```

## Start Server
```bash
python manage.py runserver
```