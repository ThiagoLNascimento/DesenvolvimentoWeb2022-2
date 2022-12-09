import locale
from decimal import Decimal

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict

from categoria.models import Categoria
from produto.carrinho import Carrinho
from produto.forms import ProdutoForm, QuantidadeForm
from produto.models import Produto



def index(request):
    return render(request, 'produto/index.html')


def lista_produto(request):
    carrinho = Carrinho(request)
    produtos_no_carrinho = carrinho.get_produtos()

    lista_de_forms = []
    for produto in produtos_no_carrinho:
        lista_de_forms.append(QuantidadeForm(
            initial={'quantidade': produto['quantidade'],
                     'produto_id': (produto['id'])}
        ))
    valor_do_carrinho = carrinho.get_preco_carrinho()

    return render(request, 'produto/lista_produto.html', {
        'listas': zip(produtos_no_carrinho, lista_de_forms),
        'valor_do_carrinho': valor_do_carrinho
    })


def cadastra_produto(request):
    if request.POST:
        produto_form = ProdutoForm(request.POST, request.FILES)

        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            produto.save()
            dic = model_to_dict(produto)

            id = dic["id"]
            categoria = produto.categoria.nome
            nome = dic["nome"]
            qtd_estoque = dic["qtd_estoque"]
            preco = dic["preco"]

            carrinho = Carrinho(request)
            carrinho.atualiza(id, qtd_estoque)
            preco_total = carrinho.get_preco_total(id)

            preco_carrinho = carrinho.get_preco_carrinho()
            locale.setlocale(locale.LC_ALL, 'pt_BR')
            preco_carrinho = locale.currency(preco_carrinho, grouping=True)
            preco_total = Decimal(preco_total)
            preco_total = locale.currency(preco_total, grouping=True)

            preco = Decimal(preco)
            preco = locale.currency(preco, grouping=True)


            return JsonResponse({'id': id,
                                 'nome': nome,
                                 'categoria': categoria,
                                 'quantidade': qtd_estoque,
                                 'preco': preco,
                                 'preco_total': str(preco_total),
                                 'preco_carrinho': str(preco_carrinho)})

    else:
        produto_form = ProdutoForm()

    return render(request, 'produto/cadastra_produto.html', {'form': produto_form})


def atualiza_produto(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        produto_id = form.cleaned_data['produto_id']
        quantidade = form.cleaned_data['quantidade']

        carrinho = Carrinho(request)
        if (quantidade == 0):
            carrinho.remover(produto_id)
            preco_total = 0.0
        else:
            carrinho.atualiza(produto_id, quantidade)
            preco_total = carrinho.get_preco_total(produto_id)

        qtd = carrinho.get_quantidade_carrinho()
        preco_carrinho = carrinho.get_preco_carrinho()


        locale.setlocale(locale.LC_ALL, 'pt_BR')
        preco_carrinho = locale.currency(preco_carrinho, grouping=True)
        preco_total = Decimal(preco_total)
        preco_total = locale.currency(preco_total, grouping=True)

        print(preco_total)

        return JsonResponse({'quantidade': qtd,
                             'preco_carrinho': preco_carrinho,
                             'preco_total': preco_total})
    else:
        raise ValueError('Ocorreu um erro inesperado ao adicionar um produto ao carrinho.')
