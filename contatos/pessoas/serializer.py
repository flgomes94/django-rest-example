from rest_framework import serializers
from .models import Pessoa
from django.contrib.auth.models import User

class PessoaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)       #define nossa id como apenas leitura
    nome = serializers.CharField(max_length=128)        #max_lenght define tamanho máximo
    telefone = serializers.CharField(max_length=20, required=False,allow_blank=True)    #pode ser em branco
    email = serializers.EmailField()
    criador =serializers.ReadOnlyField(source='criador.username')

    def create(self, validated_data):                   #se for para criar, ele usa essa fç
        return Pessoa.objects.create(**validated_data)

    def update(self, instance, validated_data):         #se for de atualizar, usa essa
        instance.nome = validated_data.get('nome', instance.nome)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    pessoas = serializers.PrimaryKeyRelatedField(many=True, queryset=Pessoa.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'pessoas')

