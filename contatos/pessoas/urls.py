from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('pessoas/', views.PessoasLista.as_view()),
    path('pessoas/<int:pk>/',views.PessoaDetalhe.as_view()),
    path('usuarios/',views.UserLista.as_view()),
    path('usuarios/<int:pk>/', views.UserDetalhe.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)