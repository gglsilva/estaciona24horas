from django.forms import ModelForm
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
    )


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'