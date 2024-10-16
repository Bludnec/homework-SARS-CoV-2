# homework-SARS-CoV-2
How start the project:

Clone the repository and enter the repository directory
```
git clone https://github.com/Bludnec/homework-SARS-CoV-2
```
Create a virtual environment
```
python3 -m venv env
```
Activate the virtual Python environment
```
source env/bin/activate   # Su Windows: env\Scripts\activate
```
Install all the requirements
```
pip install -r requirements.txt
```

Create a local PostgreSQL database, changing NAME, USER, and PASSWORD according to how it was created.
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
Run the migrations
```
python manage.py migrate
```
Start the server
```
python manage.py runserver
```
To create a user and access the ADMIN panel:
```
python manage.py createsuperuser
```
