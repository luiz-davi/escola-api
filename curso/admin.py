from django.contrib import admin

from .models import Curso, Avaliacao


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'id', 'url', 'criacao', 'atualizacao', 'ativo']


@admin.register(Avaliacao)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['curso', 'nome', 'email', 'avaliacao', 'criacao']
