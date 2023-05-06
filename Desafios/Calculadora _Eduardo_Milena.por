programa {
  funcao inicio() {
    //define suas variaveis
    inteiro n1, n2, opcao, loop;
    real resultado
    logico loop

    //variável para o loop "infinito"
    loop = verdadeiro

    //inicia o loop de calculo
    enquanto loop{
      escreva("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
      escreva("O que você quer fazer?\n1 - Somar\n2 - Subtrair\n3 - Dividir\n4 - Multiplicar\n5 - SAIR\nR: ")
      leia(opcao)
      
      // só escreve os valores se não quiser sair do código
      se (opcao != 5){
          escreva("Digite seu primeiro número: ")
          leia(n1)

          escreva("Digite seu segundo número: ")
        leia(n2)
      }

      // começa a analisar os casos
      escolha (opcao){
        caso 1:
          resultado = n1 + n2
          escreva("Você escolheu Somar, dessa forma, seu resultado é: ")
          escreva(resultado)
          escreva("\n")
          pare

        caso 2:
          resultado = n1 - n2
          escreva("Você escolheu Subtrair, dessa forma, seu resultado é: ")
          escreva(resultado)
          escreva("\n")
          pare

        caso 3:
          resultado = n1/n2
          escreva("Você escolheu Dividir, dessa forma, seu resultado é: ")
          escreva(resultado)
          escreva("\n")
          pare

        caso 4:
          resultado = n1*n2
          escreva("Você escolheu Multiplicar, dessa forma, seu resultado é: ")
          escreva(resultado)
          escreva("\n")
          pare

        caso 5:
          // finaliza o loop colocando a variável em valor lógico "falso"
          loop = falso
          pare
        caso contrario:
          escreva("opção invalida, por favor digite novamente\n")
      }
    }

    // termina o programa
    escreva("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
    escreva("Programa finalizado")
  }
}
