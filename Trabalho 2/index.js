
// Questão 1
function Proprietario(nome, sobrenome, idade, endereco, cpf, img) {
    this._nome = nome;
    this._sobrenome = sobrenome
    this._idade = idade;
    this._endereco = endereco;
    this._cpf = cpf
    this._img = img
}

// Questão 2
Object.defineProperties(Proprietario.prototype, {
    nome: {
        get: function () {
            return this._nome;
        },
        set: function (nome) {
            this._nome = nome;
        }
    },
    sobrenome: {
        get: function () {
            return this._sobrenome;
        },
        set: function (sobrenome) {
            this._sobrenome = sobrenome;
        }
    },
    idade: {
        get: function () {
            return this._idade;
        },
        set: function (idade) {
            this._idade = idade;
        }
    },
    endereco: {
        get: function () {
            return this._endereco;
        },
        set: function (endereco) {
            this._endereco = endereco;
        }
    },
    cpf: {
        get: function () {
            return this._cpf.substr(0, 3) + '.'
                + this._cpf.substr(3, 3) + '.'
                + this._cpf.substr(6, 3) + '-'
                + this._cpf.substr(9);
        },
        set: function (cpf) {
            this._cpf = cpf;
        }
    },
    img: {
        get: function () {
            return this._img;
        },
        set: function (img) {
            this._img = img;
        }
    }
})

//Questão 4
function criarObjetos(arrayObjetos) {
    let proprietarios = []
    for (let i = 0; i < arrayObjetos.length; i++) {
        proprietarios.push(new Proprietario(arrayObjetos[i].nome
            , arrayObjetos[i].sobrenome
            , arrayObjetos[i].idade
            , arrayObjetos[i].endereco
            , arrayObjetos[i].cpf
            , arrayObjetos[i].img));
    }

    return proprietarios
}

// Questão 3
const arrayObjetos = [{ nome: 'Thiago', sobrenome: 'Lopes', idade: 21, endereco: 'Rua Monerat', cpf: '11618055755', img: '/images/thiago.jpg' },
                      { nome: 'Beatriz', sobrenome: 'Nascimento', idade: 18, endereco: 'Rua Monerat', cpf: '12345678900', img: '/images/beatriz.jpeg' },
                      { nome: 'Cristiana', sobrenome: 'Pinto', idade: 49, endereco: 'Rua Desembargador', cpf: '00987654321', img: '/images/cristiana.png' }]

let proprietarios = criarObjetos(arrayObjetos)

// Questão 5
const cards = proprietarios.map(pessoa =>
    `<div class="col-sm-12" style="margin-bottom: 20px;">
        <div class="card bg-light" style="box-shadow:5px 10px 18px #888888;">
            <div class="card-body" style="height: 200px;">
                <h5 class="card-title">${pessoa.nome} ${pessoa.sobrenome}</h5>
                <p class="card-text">
                    <img src='${pessoa.img}' alt='${pessoa.nome}' style='height: 100px; width: 100px'> <br>
                    Idade: ${pessoa.idade} <br>
                    Endereço: ${pessoa.endereco} <br>
                    CPF: ${pessoa.cpf} <br>
                </p>
            </div>
        </div>
    </div>`
);

//Questão 7
const div = `<div class="row col-mb-4" style="margin-left: auto; margin-right: auto; height: 100px; width: 200px">
                ${cards.join('')}
            </div>`                


$("body").append(div);