from django import forms

from fornecedor.models import Fornecedor
from pycpfcnpj import cpfcnpj


class FornecedorForm(forms.ModelForm):

    class Meta:
        model = Fornecedor
        fields = ('nome', 'endereco', 'telefone', 'cnpj')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório para nome.',
                                            'unique': 'Nome do fornecedor duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['endereco'].error_messages = {'required': 'Campo obrigatório para endereco.'}
        self.fields['endereco'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['telefone'].error_messages = {'required': 'Campo obrigatório para telefone.'}
        self.fields['telefone'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['telefone'].empty_label = 'Digite somente os números incluindo o DDD'

        self.fields['cnpj'].error_messages = {'required': 'Campo obrigatório para CNPJ.'}
        self.fields['cnpj'].empty_label = 'Utilizar a formatação XX.XXX.XXX/XXXX-XX'
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control form-control-sm'})

