# homework-SARS-CoV-2
Clonare la repository
```
git clone https://github.com/Bludnec/homework-SARS-CoV-2
```
Entrare nella directory della repository
```
cd homework
```
Creare un environment
```
python3 -m venv env
```
Attivare il virtual python environment
```
source env/bin/activate   # Su Windows: env\Scripts\activate
```
Installare tutti i requirements
```
pip install -r requirements.txt
```

Creare un database locale postgres cambiando NAME, USER e PASSWORD in base a come è stato creato.
```
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
```
Migrare
```
python manage.py migrate
```
Lanciare il server
```
python manage.py runserver
```
Per creare utenza e accedere al pannello di ADMIN:
```
python manage.py createsuperuser
```
```
