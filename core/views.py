from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)


from .forms import(
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm)


def Home(request):
    context = {'mensagem' : 'Olá Mundo'}
    return render(request, 'core/index.html', context)

# Pessoa
def lista_pessoa(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoa.html', data)


def add_pessoa(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoa')


def upd_pessoa(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoa')

    else:
        return render(request, 'core/update_pessoa.html', data)


def del_pessoa(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == "POST":
        pessoa.delete()
        return redirect('core_lista_pessoa')
    else:
        return render(request,'core/delete_confirm.html', {'obj': pessoa})

# Veiculo
def lista_veiculo(request):
    veiculo = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculo': veiculo, 'form': form}
    return render(request, 'core/lista_veiculo.html', data)


def add_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_veiculo')


def upd_veiculo(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculo')
    else:
        return render(request, 'core/update_veiculo.html', data)

def del_veiculo(request, id):
    veiculo = Pessoa.objects.get(id=id)
    if request.method == "POST":
        veiculo.delete()
        return redirect('core_lista_veiculo')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': veiculo})

# Movimento Rotativo
def lista_mov_rota(request):
    rotativo = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rotativo': rotativo, 'form': form}
    return render(request, 'core/lista_mov_rota.html', data)


def add_mov_rota(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_mov_rota')


def upd_mov_rota(request, id):
    data = {}
    rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=rotativo)
    data['movrotativo'] = rotativo
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mov_rota')

    else:
        return render(request, 'core/update_mov_rota.html', data)


def del_mov_rota(request, id):
    rotativo = MovRotativo.objects.get(id=id)
    if request.method == "POST":
        rotativo.delete()
        return redirect('core_lista_mov_rota')
    else:
        return render(request, 'core/del_conf_mrot.html', {'obj': rotativo})


# Mensalista

def lista_mensalista(request):
    mensalista = Mensalista.objects.all()
    form = MensalistaForm()
    data = {'mensalista': mensalista, 'form': form}
    return render(request, 'core/lista_mensalista.html', data)
