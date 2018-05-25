from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Produto(models.Model):
	kategoria_choices = (
        ('IT','IT Equipment' ),
        ( 'OT','Office Stationary'),
        ('OTS','Others' ),
    )
	deskrisaun=models.CharField(max_length=255)
	kategoria=models.CharField(max_length=10,choices=kategoria_choices,default="IT Equipment")

	def __str__(self):
		return self.deskrisaun


class Fornesedor(models.Model):
	nasaun_choice=(
		('TL','Timor Leste'),
		('IN','Indonesia'),
		)
	fornecedor=models.CharField(max_length=20)
	morada=models.CharField(max_length=30)
	cidade=models.CharField(max_length=30)
	Nasaun=models.CharField(max_length=30,choices=nasaun_choice, default='Timor Leste')

	def __str_(self):
		self.fornecedor

class Titulo(models.Model):
	titulo=models.CharField(max_length=40)
	def __str__(self):
		return self.titulo
		pass

class Employer(models.Model):
	naran=models.CharField(max_length=40)
	titulo=models.ForeignKey(Titulo,on_delete=models.CASCADE)
	#titulo=models.CharField(max_length=30)
	address=models.CharField(max_length=43)
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Numeru tenke iha formatu tuir mai: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list

	def __str__(self):
		return self.naran
		pass

class Order(models.Model):
	deskrisaun=models.CharField(max_length=40)
	data_requijisaun=models.DateTimeField(auto_now=True)
	data_entrega=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.deskrisaun
		pass