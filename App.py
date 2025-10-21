import datetime
import locale

# Define o idioma para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Pergunta o nome da pessoa
nome = input("Qual é o seu nome?: ").strip().title()

# Pergunta se a pessoa faltou
resposta = input(f"{nome}, você faltou? (sim/não): ").strip().lower()

if resposta == "sim":
    dia_str = input("Qual dia você faltou? (formato: DD/MM/AAAA): ").strip()
    try:
        # Converte a string para um objeto de data
        dia = datetime.datetime.strptime(dia_str, "%d/%m/%Y")
        dia_semana = dia.weekday()  # 0 = segunda, 6 = domingo
        nome_dia = dia.strftime("%A")  # Nome do dia em português

        # Verifica se é fim de semana ou dia útil
        if dia_semana >= 5:
            horas_devidas = 4
        else:
            horas_devidas = 5

        print(f"{nome}, falta registrada em {nome_dia} ({dia_str}). Você deve {horas_devidas} horas.")
    except ValueError:
        print("Data inválida. Use o formato DD/MM/AAAA.")
elif resposta == "não":
    print(f"Sem problemas, {nome}. Presença confirmada.")
else:
    print("Resposta inválida. Por favor, digite 'sim' ou 'não'.")
