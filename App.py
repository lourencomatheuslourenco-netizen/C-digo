import streamlit as st
import datetime
import locale

# Define o idioma para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

st.title("Registro de Faltas")

# Entrada do nome
nome = st.text_input("Qual é o seu nome?")

# Verifica se o nome foi preenchido
if nome:
    # Pergunta se a pessoa faltou
    resposta = st.radio(f"{nome}, você faltou?", ["Sim", "Não"])

    if resposta == "Sim":
        dia_str = st.text_input("Qual dia você faltou? (formato: DD/MM/AAAA)")

        if dia_str:
            try:
                # Converte a string para data
                dia = datetime.datetime.strptime(dia_str, "%d/%m/%Y")
                dia_semana = dia.weekday()
                nome_dia = dia.strftime("%A")

                # Calcula horas devidas
                horas_devidas = 4 if dia_semana >= 5 else 5

                st.success(f"{nome}, falta registrada em {nome_dia} ({dia_str}). Você deve {horas_devidas} horas.")
            except ValueError:
                st.error("Data inválida. Use o formato DD/MM/AAAA.")
    else:
        st.info(f"Sem problemas, {nome}. Presença confirmada.")
