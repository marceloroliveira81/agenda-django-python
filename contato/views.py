from django.shortcuts import render

from .models import Contato

from .forms import ContatoForm

# Create your views here.

def index(request):
	contatos = Contato.objects.all()
	return render(request, 'contato/index.html', {'contatos' : contatos})

def detalhes(request, pk):
	contato = Contato.objects.get(pk=pk)
	return render(request, 'contato/detalhes.html', {'contato' : contato})

def novo(request):
	#if request.method == 'POST':
	#	if form.is_valid():
	
	#else: 
	form = ContatoForm()
	
	return render(request, 'contato/novo.html', {'form' : form})
