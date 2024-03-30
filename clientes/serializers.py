from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de cpf inválido'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome não pode conter numeros'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O rg deve ter 9 digitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'Digite um número válido seguindo o modelo. Ex.:11 91234-1234'})
        return data