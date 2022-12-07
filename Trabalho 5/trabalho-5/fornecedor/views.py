from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from fornecedor.forms import FornecedorForm
from fornecedor.models import Fornecedor


def lista_fornecedor(request):
    lista_de_fornecedores = Fornecedor.objects \
                            .order_by('nome')
    # Criação de um objeto da classe Paginator tendo como atributos a lista de objetos e a quantidade de objetos por página
    paginator = Paginator(lista_de_fornecedores, 4)
    # Recupera o parâmetros de requisição denominado pagina enviado para o servidor no momento de uma requisição do tipo
    # GET, na primeira execução o valor é none
    pagina = request.GET.get('pagina')
    # Retorna um objeto do tipo page que representa a primeira página da paginação
    page_obj = paginator.get_page(pagina)

    print(pagina)
    return render(request, 'fornecedor/pesquisa_fornecedor.html', {'fornecedores': page_obj })


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

            # É usado um redirect no lugar do render para evitar o envio de um duplo POST, o que poderia causar
            # o envio de um formulário repetido e salvar os dados mais de uma vez no banco de dados
            # Nesse caso irá procurar a url exibe_fornecedor passando como parâmetro o id do fornecedor
            return redirect('fornecedor:exibe_fornecedor', id=fornecedor.id)
    else:
        try:
            del request.session['fornecedor_id']
        except KeyError:
            pass
        fornecedor_form = FornecedorForm()

    return render(request, 'fornecedor/cadastra_fornecedor.html', {'form': fornecedor_form})


def exibe_fornecedor(request, id):
    # Buscar o da classe Fornecedor cuja chave primária tem o valor id, causando um erro 404 caso não seja possível e
    # parando a execução da view
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    # Salva no objeto de sessão o id do fornecedor cuja chave é fornecedor_id_del, para ser usado no momento da deleção
    request.session['fornecedor_id_del'] = id
    return render(request, 'fornecedor/exibe_fornecedor.html', {'fornecedor': fornecedor})


def edita_fornecedor(request, id):
    fornecedor = get_object_or_404(Fornecedor, pk=id)
    # Crição de um objeto da classe FornecedorForm usando como instância o objeto fornecedor encontrado anteriormente
    fornecedor_form = FornecedorForm(instance=fornecedor)
    # O uso de chaves diferentes é feito facilitar a detecção e teste de problemas, visto que um bug na execução
    # dessa view, poderia atrapalhar o funcionamento da outra view
    # É feito isso para salvar o id do fornecedor no objeto sessão, visto que o id não é um campo presente no formulário
    request.session['fornecedor_id'] = id
    return render(request, 'fornecedor/cadastra_fornecedor.html', {'form': fornecedor_form})


def remove_fornecedor(request):
    fornecedor_id = request.session.get('fornecedor_id_del')
    fornecedor = get_object_or_404(Fornecedor, id=fornecedor_id)
    fornecedor.delete()
    del request.session['fornecedor_id_del']
    messages.add_message(request, messages.INFO, 'Fornecedor removido com sucesso.')
    return render(request, 'fornecedor/exibe_fornecedor.html', {'fornecedor': fornecedor})
