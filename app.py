import streamlit as st

# Configuração da página para um visual mais limpo
st.set_page_config(
    page_title="Calculadora Vibe",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa Vibe")
st.markdown("Bem-vindo(a) ao seu primeiro aplicativo web em Python com Streamlit!")

# Linha divisória estética
st.markdown("---")

# 2. Dois campos de entrada numérica
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("Digite o 1º número:", value=0.0, format="%.2f")
with col2:
    num2 = st.number_input("Digite o 2º número:", value=0.0, format="%.2f")

# 3. Componente de seleção para escolher a operação
operacao = st.selectbox(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)")
)

st.markdown("---")

# 4. Botão de ação
if st.button("Calcular", type="primary", use_container_width=True):
    # 5. Processamento e regras de negócio
    resultado = None
    erro = None

    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        if num2 == 0:
            erro = "Ops! Divisão por zero não é permitida. Tente outro valor para o segundo número."
        else:
            resultado = num1 / num2

    # Exibição amigável do resultado ou erro
    if erro:
        st.error(erro)
    else:
        # Dispara o efeito de balões na tela
        st.balloons()
        
        st.success("Cálculo realizado com sucesso!")
        st.metric(label="Resultado Final", value=f"{resultado:,.4f}")
        