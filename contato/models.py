from django.db import models

# Create your models here.

class Contato(models.Model):
	
	SEXO = (
		('F', 'Feminino'),
		('M', 'Masculino')
	)

	ESTADO_CIVIL = (
		('1', 'Solteiro(a)'),
		('2', 'Casado(a)'),
		('3', 'Viúvo(a)'),
		('4', 'Divorciado(a)'),
		('5', 'Separado(a)')
	)

	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	sexo = models.CharField(max_length=1, choices=SEXO)
	estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.nome