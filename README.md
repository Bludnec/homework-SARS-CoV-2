# homework-SARS-CoV-2

git clone https://github.com/Bludnec/homework-SARS-CoV-2
cd homework
python3 -m venv env
source env/bin/activate   # Su Windows: env\Scripts\activate
pip install -r requirements.txt

Creare un database locale postgres cambiando NAME, USER e PASSWORD in base a come è stato creato.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

python manage.py migrate
python manage.py runserver

Per creare utenza e accedere al pannello di ADMIN:
python manage.py createsuperuser
