from .models import Pessoa
from .serializer import PessoaSerializer,UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

from rest_framework import generics

'''
As views utilizam o conceito de class-based-view. Onde cada view é vista como uma classe.
Existem uns recursos ainda a mais aqui dentro que o Django Rest Framework facilita pra gente
Percebam conceitos como herança, sobrecarga, sobreposição e tudo mais nessas views.
'''

class PessoasLista (generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def perform_create(self, serializer):
        serializer.save(criador=self.request.user)


class PessoaDetalhe (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class UserLista (generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetalhe(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

