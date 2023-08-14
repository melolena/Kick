
'''

#soma sem argumentos

#criar função
def ola_mundo():
    print('Olá mundo!')

#chama fução
#ola_mundo()


#soma com argumentos
def soma(n1,n2):
    soma = n1 + n2
    print(soma)

soma(10,5)
soma(12,50)

#argumentos arbiteários

def pessoas(*nomes):
    print(nomes)

pessoas('Milena', 'Thalita', 'Mariane')
pessoas('Julia', 'Flávia')
'''
#dicionário
produto_codigo = {}

def cadastrar_produtos():
    codigo = input('Digite o código do produto: ')
    nome =  input('Digite o nome do produto: ')
    preco =  float(input('Digite o preço do produto: '))
    estoque = int( input('Digite a quantidade em estoque: '))


    produto = {
        'nome':nome,
        'preco':preco,
        'estoque':estoque
    }

    produto_codigo[codigo] = produto
    print('produto cadastrado com sucesso')

'''
def listar_produtos():
    print('lista de produtos: ')
    for codigo, produto in produto_codigo.items():
        print(f'Código: {codigo}, Nome:{produto['nome']}, preçço:{produto['preco']}'),quantidade
        
    '''