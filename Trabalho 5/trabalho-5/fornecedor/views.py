from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from fornecedor.forms import FornecedorForm
from fornecedor.models import Fornecedor


def lista_fornecedor(request):
    pass


def cadastra_fornecedor(request):

    if request.POST:
        fornecedor_id = request.session.get('fornecedor_id')
        print('fornecedor_id na sessão = ' + str(fornecedor_id))
        if fornecedor_id:
            fornecedor = get_object_or_404(Fornecedor, pk=fornecedor_id)
            fornecedor_form = FornecedorForm(request.POST, request.FILES, instance=fornecedor)
        else:
            fornecedor_form = FornecedorForm(request.POST, request.FILES)

        if fornecedor_form.is_valid():
            fornecedor = fornecedor_form.save()
            if fornecedor_id:
                messages.add_message(request, messages.INFO, 'Fornecedor alterado com sucesso!')
                del request.session['fornecedor_id']
            else:
                messages.add_message(request, messages.INFO, 'Fornecedor cadastrado com sucesso!')

            return redirect('fornecedor:exibe_fornecedor', id=fornecedor.id)
    else:
        try:
            del request.session['fornecedor_id']
        except KeyError:
            pass
        fornecedor_form = FornecedorForm()

    return render(request, 'fornecedor/cadastra_fornecedor.html', {'form': fornecedor_form})


def exibe_fornecedor(request):
    pass


def edita_fornecedor(request):
    pass

def remove_fornecedor(request):
    pass