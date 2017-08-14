from django.shortcuts import render

from .models import Contato

# Create your views here.

def index(request):
	contatos = Contato.objects.all()
	return render(request, 'contato/index.html', {'contatos' : contatos})

def detalhes(request, pk):
	contato = Contato.objects.get(pk=pk)
	return render(request, 'contato/detalhes.html', {'contato' : contato})