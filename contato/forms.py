from django import forms

from .models import Contato

#class ContatoForm(forms.Form):
#	nome = forms.CharField(label = 'Nome:', max_length=200)

class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato
		fields = ('nome', 'data_nascimento', 'sexo', 'estado_civil', 'email')
