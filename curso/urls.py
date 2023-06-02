from django.urls import path

from . import views


urlpatterns = [
    path('cursos/', views.CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>', views.CursoAPIView.as_view(), name='curso'),
    path('avaliacoes/', views.AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:pk>', views.AvaliacaoAPIView.as_view(), name='avaliacao'),
]
