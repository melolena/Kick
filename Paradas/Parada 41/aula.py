from datetime import date, datetime, timedelta

hoje = date.today()
print(hoje.strftime('%d/%m/%y'))

agora = datetime.now()

print(agora)

#operações com data
ontem = hoje -timedelta(days=1)

print(ontem)

hoje2 = date.today().strftime('%A') #porcentagem mostra o dia da semana

print(hoje2)

#uma linha

"""
mais de uma linha

nome = "Milena"
sexo = "F"
idade = 23
altura = 1.58

print(nome, sexo, idade, altura)

print("Olá mundo!")

dia = "domingo"
print(dia)

d = 10 
mm = 9
aa = 2023
print("Dia: ",d, "mes: ",mm, "Ano: ",aa)

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

print(nome)

#verificando  otipo da variável
print(type(idade))



#m para cm * 100
# input 
# processamento 
# saída (print)

m = int(input("Digite um valor em m: "))
cm = m * 100

print(cm)



#media aritimética
#input 2 valores
#processamento 
#saída

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))

ma = (num1+num2)/2
print("A média aritimética é: ",ma)


"""