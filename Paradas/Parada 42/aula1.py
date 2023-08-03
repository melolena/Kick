from datetime import date, datetime, timedelta

# pega o nome do dia da semana
hoje = date.today().strftime("%A")


# operacoes com data
#ontem = hoje - timedelta(days=1)

print(hoje)

