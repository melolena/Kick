idade = 16

if idade > 20:
    print("jovem")
elif idade >= 20 or idade < 65:
    print("aldulto")
else:
    print("idoso")


# 1  ============
# bloco try
try:
    # Solicita o número de maçãs compradas ao usuário
    macas_compradas = int(input("Digite o número de maçãs compradas: "))

    # Calcula o valor total da compra

    if macas_compradas < 12:
        valor_total = macas_compradas * 0.30
    else:
        valor_total = macas_compradas * 0.25

    # Exibe o valor total da compra
    print(f"O valor total da compra é R$ {valor_total:.2f}")
except:
    print("valor incorreto, digite um valor inteiro")

# 2 ===================

from datetime import datetime

# Obtém a hora atual
hora_atual = datetime.now().hour

# Verifica a hora e exibe a mensagem apropriada
if hora_atual >= 18 or hora_atual < 5:
    print("Boa noite")
elif hora_atual >= 5 and hora_atual < 12:
    print("Bom dia")
else:
    print("Boa tarde")

