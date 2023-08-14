
notas_alunos = {}

def inserir_notas():
  nome = input('insira o nome do aluno: ')
  nota1 = float(input('insira a nota da primeira unidade: '))
  nota2 = float(input('insira a nota da segunda unidade: '))
  nota3 = float(input('insira a nota da terceira unidade: '))
  nota4 = float(input('insira a nota da quarta unidade: '))

  notas = {
      'nome': nome,
      'nota1': nota1,
      'nota2': nota2,
      'nota3': nota3,
      'nota4': nota4
  }

  notas_alunos[nome] = notas
  print('Aluna cadastrado com sucesso!')


#calcular média
def calcular_media():
      for nome, notas in notas_alunos.items():
         media = (notas['nota1'] + notas['nota2'] + notas['nota3'] + notas['nota4']) / 4
         print(f'A média do aluno: {nome} é {media:.1f}')

#exibir notas e alunos

def exibir_alunos():
    print('Alunos')
    for nome, notas in notas_alunos.items():
        print(f'Aluno: {nome}')
        print(f'  U1: {notas["nota1"]}')
        print(f'  U2: {notas["nota2"]}')
        print(f'  U3: {notas["nota3"]}')
        print(f'  U4: {notas["nota4"]}')

  

def main():
    while True:
      print('Banco de notas')
      print('1 - Inserir nota dos alunos')
      print('2 - Médias')
      print('3 Notas por unidade')
      print('4 - sair')

      escolha = int(input('Escolha uma opção: '))

      if escolha == 1:
        inserir_notas()
      elif escolha == 2:
        calcular_media()
      elif escolha == 3:
        exibir_alunos()
      elif escolha == 4:
        print('Até logo!')
        break

if __name__ == "__main__":
   main()



