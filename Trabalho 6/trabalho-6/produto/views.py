from django.core.signing import Signer
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms.models import model_to_dict

from produto.carrinho import Carrinho
from produto.forms import ProdutoForm, QuantidadeForm
from produto.models import Produto

signer = Signer()


def index(request):
    return render(request, 'produto/index.html')


def lista_produto(request):
    carrinho = Carrinho(request)
    produtos_no_carrinho = carrinho.get_produtos()

    lista_de_forms = []
    for produto in produtos_no_carrinho:
        lista_de_forms.append(QuantidadeForm(
            initial = {'quantidade': produto['quantidade'],
                       'produto_id': signer.sign(produto['id'])}
        ))
    valor_do_carrinho = carrinho.get_preco_carrinho()

    return render (request, 'produto/lista_produto.html', {
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
            categoria = dic["categoria"]
            nome = dic["nome"]
            qtd_estoque = dic["qtd_estoque"]
            preco = dic["preco"]
            preco_total = float(preco) * int(qtd_estoque)
            print(preco_total)


            return JsonResponse({'id': id,
                                 'nome': nome,
                                 'categoria': categoria,
                                 'quantidade': qtd_estoque,
                                 'preco': preco,
                                 'preco_total': str(preco_total)})

    else:
        produto_form = ProdutoForm()

    return render(request, 'produto/cadastra_produto.html', {'form': produto_form})


def remove_produto(request):
    pass


def atualiza_produto(request):
    pass
