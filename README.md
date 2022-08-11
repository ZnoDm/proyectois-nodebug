# BoutiqueMegaCentro
IS I
Cambir el nombre del proyecto descargado a:
	
	proyectois

PRIMER PASO: 
===============          CRISPY-FORMS          ===============

	pip install django-crispy-forms

SEGUNDO PASO:
===============         BASE DE DATOS          ==================

Base de Datos en TERMINAL:

	pip3 list
	pip3 install PyMySQL
	

__init__.py:

	import pymysql
	pymysql.install_as_MySQLdb()

settings configuramos la conexión con MYSQL:

	DATABASES = {
	    'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'examen2',
		'USER': 'root',
		'PASSWORD': '',
		'HOST': 'localhost',
		'PORT': '3306',
		}
	}

Ejecutamos los commandos para que aparezcan las tablas. 

	python manage.py makemigrations
	python manage.py migrate
  
TERCER PASO:
===============        Ejecutando proyecto        ==================

	python manage.py runserver
