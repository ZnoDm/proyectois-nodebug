# BoutiqueMegaCentro
IS I

PRIMER PASO: 
Cambiar el nombre del proyecto descargado a:
	
	proyectois

SEGUNDO PASO: 
===============          CRISPY-FORMS          ===============

En la terminal:

	pip install django-crispy-forms

TERCER PASO:
===============         BASE DE DATOS          ==================

En la terminal:

	pip3 list
	pip3 install PyMySQL
	

En el archivo proyectois/__init__.py:

	import pymysql
	pymysql.install_as_MySQLdb()

settings configuramos la conexión con MYSQL:

	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'test01',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '3306',
		}
	}

Ejecutamos los commandos para que aparezcan las tablas. 

	python manage.py makemigrations
	python manage.py migrate
  

===============        Ejecutando proyecto        ==================

	python manage.py runserver
