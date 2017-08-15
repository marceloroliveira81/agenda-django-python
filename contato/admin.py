from django.contrib import admin

from django.contrib.admin import AdminSite

from .models import Contato

# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'data_nascimento', 'email', 'sexo', 'estado_civil')
	list_filter = ('sexo', 'estado_civil')
	search_fields = ['nome']

admin.site.register(Contato, ContatoAdmin)

class CustonAdminSite(AdminSite):
	site_header = 'Agenda - Contatos'
	site_title = 'Agenda - Contatos'
	index_title = 'Administração'

admin_site = CustonAdminSite(name='myadmin')
admin_site.register(Contato, ContatoAdmin)