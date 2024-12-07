from senha import API_KEY
import streamlit as st 
import requests
import json

# Configurações de cabeçalhos e links
headers_1 = {"Authorization": f"Bearer {API_KEY}"}
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link_1 = "https://api.openai.com/v1/chat/completions"
link = "https://api.openai.com/v1/models"
id_modelo = "gpt-4o-mini-2024-07-18"

# Entrada do usuário no Streamlit
texto = st.text_input("Faça sua pergunta:")

# Corpo da mensagem
if texto:
    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user", "content": texto}]
    }
    body_mensagem = json.dumps(body_mensagem)

    # Requisição para chat/completions
    requisicao_1 = requests.post(link_1, headers=headers, data=body_mensagem)

# Requisição para listar modelos
requisicao = requests.get(link, headers=headers_1)

# Navegação
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Selecione uma página", ["Página 1: Modelos", "Página 2: Gráficos", "Página 3: Resultados"])

if pagina == "Página 1: Modelos":
    st.title("Página 1: Modelos")
    if requisicao.status_code == 200:
        st.write("Modelos disponíveis:")
        st.write(requisicao.json())
    else:
        st.error(f"Erro {requisicao.status_code}: {requisicao.text}")

elif pagina == "Página 2: Gráficos":
    st.title("Página 2: Gráficos")
    if texto and requisicao_1.status_code == 200:
        st.write("Resposta do chat/completions:")
        st.write(requisicao_1.json())
    elif texto:
        st.error(f"Erro {requisicao_1.status_code}: {requisicao_1.text}")
    else:
        st.write("Por favor, insira uma pergunta.")
