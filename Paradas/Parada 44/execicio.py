
def pesquisa_prefeitura():
    total_salarios = 0
    total_filhos = 0
    maior_salario = 0
    total_pessoas = 0
    salario_ate_350 = 0

    while True:
        salario = float(input('Digite o salário: '))
        if salario == 0:
            break
        
        total_salarios += salario
        
        filhos = int(input('Digite o número de filhos: '))
        total_filhos += filhos
        
        if salario > maior_salario:
            maior_salario = salario
        
        if salario <= 350:
            salario_ate_350 += 1
        
        total_pessoas += 1

    media_salarios = total_salarios / total_pessoas
    media_filhos = total_filhos / total_pessoas
    percentual_ate_350 = (salario_ate_350 / total_pessoas) * 100

    print(f'Média de salário da população: R${media_salarios:.2f}')
    print(f'Média de filhos por pessoa: {media_filhos:.2f}')
    print(f'Maior salário: R${maior_salario:.2f}')
    print(f'Percentual de pessoas com salário até R$350,00: {percentual_ate_350:.2f}%')

pesquisa_prefeitura()
    
          

'''

def subtracao(a,b):
  calculo =  a - b
  print(calculo)

subtracao(4,6)


def media_anual():
  n1 = float(input('Insira a primeira nota: '))
  n2 = float(input('Insira a segunda nota: '))
  n3 = float(input('Insira a terceira nota: '))
  n4 = float(input('Insira a quarta nota: '))

  media = (n1 + n2 + n3 + n4) /4

  if media >= 7:
    print(f'Média:{media} Aprovado por média!')
  else:
        print(f'Média {media} Reprovado por média')

media_anual()


def argumentos():
    n1 = float(input('Digite o primeiro valor:'))
    n2 = float(input('Digite o segundo valor:'))
    n3 = float(input('Digite o terceiro valor:'))

    produto = n1 * n2 * n3

    print(f'a multiplicação de {n1}, {n2} e {n3} é: {produto}')


argumentos()

def atleta(): 
    print('Categoria natação por idade')
    idade = int(input('Digite a idade: '))
    
    if idade >= 5 and idade <=7:
        print('Categoria infantil A')
    
    elif idade >= 8 and idade <= 10:
        print('Categoria infatil B')
    
    elif idade >= 11 and idade <= 13:
        print('Categoria juvenil A')

    elif idade >= 14 and idade <= 17:
        print('Categoria Juvenil B')
    
    elif idade >= 18:
        print('Categoria adulto')

atleta()

def numero_perfeito():
    soma_divisores = 0
    valor = int(input('insira um número: '))

    for divisor in range(1, valor):
        if valor % divisor == 0:
            soma_divisores += divisor
        
    if soma_divisores == valor:
        print('Número perfeito!')
    else:
        print('Não é um númeor perfeito')

numero_perfeito()



'''
