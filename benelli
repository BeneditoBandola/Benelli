import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Benelli Confecções - Orçamentos e Medidas",
    page_icon="👕",
    layout="wide",
)

# Dados de Preços baseados na tabela oficial da Benelli (20/04/2026)
TABELA_TECIDOS = {
    "Meia Malha Cardada - Branca": {"avista": 36.16, "prazo": 36.90},
    "Meia Malha Cardada - Escura": {"avista": 46.94, "prazo": 47.90},
    "Meia Malha Penteada - Branca": {"avista": 44.98, "prazo": 45.90},
    "Meia Malha Penteada - Clara": {"avista": 51.84, "prazo": 52.90},
    "Meia Malha Penteada - Média": {"avista": 53.80, "prazo": 54.90},
    "Meia Malha Penteada - Escura": {"avista": 55.66, "prazo": 56.80},
    "Meia Malha Poliéster Fiado - Branca": {"avista": 30.48, "prazo": 31.10},
    "Meia Malha Poliéster Fiado - Escura": {"avista": 34.79, "prazo": 35.50},
    "Meia Malha Dry Fit / Dry Sport - Branca": {"avista": 37.14, "prazo": 37.90},
    "Meia Malha Dry Fit / Dry Sport - Escura": {"avista": 41.65, "prazo": 42.50},
    "Moletom Flanelado Cores": {"avista": 52.43, "prazo": 53.50},
    "Suedine P.A. Cores": {"avista": 53.80, "prazo": 54.90},
}

st.title("👕 Benelli Confecções - Sistema de Orçamentos")
st.markdown(
    "**Contacto:** (35) 98846-6651 | Confeccionamos peças sob medida[cite: 11, 13]."
)

# Criação das Abas para separar a visão do Cliente e do Orçamento
aba_cliente, aba_orcamento = st.tabs(
    ["👀 Visualizador para o Cliente", "🧮 Criar Orçamento"]
)

with aba_cliente:
  st.header("Guia de Tamanhos e Medidas")
  st.markdown(
      "Explore abaixo os tamanhos disponíveis para camisetas adultas, infantis"
      " e baby look."
  )

  tipo_tabela = st.selectbox(
      "Selecione a categoria:",
      ["Camisetas Adultas", "Tamanhos Infantis", "Tamanhos Baby Look"],
  )

  if tipo_tabela == "Camisetas Adultas":
    st.subheader("Medidas de Camisetas Adultas")
    col1, col2, col3 = st.columns(3)
    with col1:
      st.info(
          "**PP:** 62 cm (Altura) x 48 cm (Largura)\n\n**P:** 68 cm x 51"
          " cm[cite: 10]"
      )
    with col2:
      st.info(
          "**M:** 70 cm (Altura) x 52 cm (Largura)\n\n**G:** 73 cm x 57"
          " cm[cite: 10]"
      )
    with col3:
      st.info(
          "**GG:** 75 cm (Altura) x 58 cm (Largura)\n\n**XG:** 79 cm x 62"
          " cm\n\n**XGG:** 81 cm x 68 cm[cite: 10]"
      )

  elif tipo_tabela == "Tamanhos Infantis":
    st.subheader("Medidas Infantis (Tamanhos 1 ao 14)")
    st.write(
        "• **Tamanho 1:** 33 cm x 28 cm[cite: 11]\n• **Tamanho 2:** 37 cm x"
        " 28.5 cm[cite: 11]\n• **Tamanho 3:** 40 cm x 31 cm[cite: 11]\n•"
        " **Tamanho 4:** 44 cm x 33 cm[cite: 11]\n• **Tamanho 6:** 47.5 cm x"
        " 36.5 cm[cite: 11]\n• **Tamanho 8:** 52.5 cm x 39 cm[cite: 11]\n•"
        " **Tamanho 10:** 55.5 cm x 41.5 cm[cite: 11]\n• **Tamanho 12:** 60 cm"
        " x 45 cm[cite: 11]\n• **Tamanho 14:** 64 cm x 47.5 cm[cite: 11]"
    )

  elif tipo_tabela == "Tamanhos Baby Look":
    st.subheader("Medidas de Baby Look")
    st.write(
        "• **P:** 62 cm x 44 cm[cite: 13]\n• **M:** 63 cm x 45 cm[cite: 13]\n•"
        " **G:** 66 cm x 47 cm[cite: 13]\n• **GG:** 68 cm x 49 cm[cite: 13]\n•"
        " **XG:** 69 cm x 50 cm[cite: 13]"
    )

with aba_orcamento:
  st.header("Gerador de Orçamentos")

  cliente_nome = st.text_input("Nome do Cliente:")
  tecido_escolhido = st.selectbox(
      "Escolha o Tecido / Composição:", list(TABELA_TECIDOS.keys())
  )
  condicao_pagamento = st.radio(
      "Condição de Pagamento:", ["À Vista", "A Prazo"]
  )
  quantidade = st.number_input(
      "Quantidade de Peças:", min_value=1, value=10, step=1
  )

  # Cálculo do valor
  if condicao_pagamento == "À Vista":
    preco_unitario = TABELA_TECIDOS[tecido_escolhido]["avista"]
  else:
    preco_unitario = TABELA_TECIDOS[tecido_escolhido]["prazo"]

  valor_total = preco_unitario * quantidade

  st.divider()
  st.subheader("Resumo do Orçamento")
  st.write(f"**Cliente:** {cliente_nome if cliente_nome else 'Não informado'}")
  st.write(f"**Tecido:** {tecido_escolhido}")
  st.write(f"**Quantidade:** {quantidade} unidades")
  st.write(f"**Preço Unitário ({condicao_pagamento}):** R$ {preco_unitario:.2f}")
  st.markdown(
      f"### **Valor Total:** R$ {valor_total:.2f}"
  )

  if st.button("Gerar Texto para WhatsApp"):
    texto_wpp = (
        f"*ORÇAMENTO - BENELLI CONFECÇÕES*\n"
        f"Olá {cliente_nome}, segue a sua cotação:\n\n"
        f"• *Tecido:* {tecido_escolhido}\n"
        f"• *Quantidade:* {quantidade} peças\n"
        f"• *Condição:* {condicao_pagamento}\n"
        f"• *Valor Unitário:* R$ {preco_unitario:.2f}\n"
        f"• *Total:* *R$ {valor_total:.2f}*\n\n"
        f"Entre em contacto pelo telefone (35) 98846-6651[cite: 11, 13]."
    )
    st.text_area("Copie o texto abaixo para enviar:", texto_wpp, height=150)
