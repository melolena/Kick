programa {
  funcao inicio() {
    //define suas variaveis
    inteiro n1, n2, opcao, loop;
    real resultado
    logico loop

    //vari�vel para o loop "infinito"
    loop = verdadeiro

    //inicia o loop de calculo
    enquanto loop{
      escreva("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
      escreva("O que voc� quer fazer?\n1 - Somar\n2 - Subtrair\n3 - Dividir\n4 - Multiplicar\n5 - SAIR\nR: ")
      leia(opcao)
      
      // s� escreve os valores se n�o quiser sair do c�digo
      se (opcao != 5){
          escreva("Digite seu primeiro n�mero: ")
          leia(n1)

          escreva("Digite seu segundo n�mero: ")
        leia(n2)
      }

      // come�a a analisar os casos
      escolha (opcao){
        caso 1:
          resultado = n1 + n2
          escreva("Voc� escolheu Somar, dessa forma, seu resultado �: ")
          escreva(resultado)
          escreva("\n")
          pare

        caso 2:
          resultado = n1 - n2
          escreva("Voc� escolheu Subtrair, dessa forma, seu resultado �: ")
          escreva(resultado)
          escreva("\n")
          pare

        caso 3:
          resultado = n1/n2
          escreva("Voc� escolheu Dividir, dessa forma, seu resultado �: ")
          escreva(resultado)
          escreva("\n")
          pare

        caso 4:
          resultado = n1*n2
          escreva("Voc� escolheu Multiplicar, dessa forma, seu resultado �: ")
          escreva(resultado)
          escreva("\n")
          pare

        caso 5:
          // finaliza o loop colocando a vari�vel em valor l�gico "falso"
          loop = falso
          pare
        caso contrario:
          escreva("op��o invalida, por favor digite novamente\n")
      }
    }

    // termina o programa
    escreva("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
    escreva("Programa finalizado")
  }
}
