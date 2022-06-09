from pyexpat import model
from django.db import models

# Create your models here.

## creo los modelos para determinar la base de datos

class Familiares (models.Model):  #las clasese eredan models.Model

    nombre = models.CharField(max_length=40)    ## me permite ingresar datos char (texto)
    edad = models.IntegerField()                ## numero entero
    ##nacimiento = models.DateField()             ## me permite pasar una fecha

class Amigos (models.Model):

    nombre = models.CharField(max_length=40)    
    edad = models.IntegerField()            
    ##nacimiento = models.DateField()

class Clientes (models.Model):

    nombre = models.CharField(max_length=40)    
    edad = models.IntegerField()            
    ##nacimiento = models.DateField()

## terminados los modelos puedo preparar la base de datos para la migracion

## creo la proforma de la base de datos con:
## python manage.py makemigrations

## una vez se crea la base de datos (db.sqlite3)

## migramos los modelos a la base de datos con:
## python manage.py sqlmigrate personas 0001  (nombre de la app + el numero de la migracion preparada)

## migro los modulos listos con python manage.py migrate para que impacten en la base de datos y se armen las tablas