from django.shortcuts import render, redirect, get_object_or_404

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
	if request.method == 'POST':
		form = ContatoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')

	else: 
		form = ContatoForm()
	
	return render(request, 'contato/novo.html', {'form' : form})

def alterar(request, pk):
	contato = get_object_or_404(Contato, pk=pk)
	if request.method == 'POST':
		form = ContatoForm(request.POST, instance=contato)
		if form.is_valid():
			form.save()
			return redirect('index')
	
	else: 
		form = ContatoForm(instance=contato)
	
	return render(request, 'contato/novo.html', {'form' : form})

def excluir(request, pk):
	contato = get_object_or_404(Contato, pk=pk)
	contato.delete()
	return redirect('index')
	#contatos = Contato.objects.all()
	#return render(request, 'contato/index.html', {'contatos' : contatos})