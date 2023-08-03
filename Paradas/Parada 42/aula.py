#atividade 1
try: 
    qtd = int(input('Quantas maçãs você quer? '))

    if qtd < 12:
        total = qtd * 0.30
        print(f'Sua compra deu: R${total:.2f}')
    else:
        total = qtd * 0.25
        print (f'Sua compra deu: R${total:.2f}')

        #atividade 2

        

        
except: print('Valor incorreto, tente novamente')

#atividade 2
from datetime import datetime

hora_atual = datetime.now().hour

if hora_atual >= 18 or hora_atual < 5:
    print('Boa noite')
elif hora_atual >= 5 and hora_atual< 12:
    print ('Bom dia')
else: 
    print ('Boa tarde')

"""
idade = 25

if idade > 18:
    print('Jovem')
elif idade >= 20 and idade <65:
    print('adulto')
else:
    print ('idoso')
"""