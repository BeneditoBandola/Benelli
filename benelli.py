import base64
import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Benelli Confecções - Orçamentos e Medidas",
    page_icon="👕",
    layout="wide",
)

# Estilo visual personalizado (CSS)
st.markdown(
    """
    <style>
        .main { background-color: #f8f9fa; }
        .stTabs [data-baseweb="tab-list"] { gap: 10px; }
        .stTabs [data-baseweb="tab"] {
            background-color: #ffffff;
            border-radius: 8px 8px 0px 0px;
            padding: 10px 20px;
            font-weight: bold;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .stTabs [aria-selected="true"] {
            background-color: #2c3e50 !important;
            color: white !important;
        }
        div.stButton > button:first-child {
            background-color: #27ae60;
            color: white;
            font-weight: bold;
            border-radius: 6px;
            width: 100%;
            padding: 10px;
        }
        div.stButton > button:first-child:hover {
            background-color: #219653;
        }
    </style>
""",
    unsafe_allow_html=True,
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

# Cabeçalho Principal
st.title("👕 Benelli Confecções")
st.markdown("##### *Sistema Profissional de Orçamentos e Consulta de Medidas*")
st.info(
    "📞 **Contato direto:** (35) 98846-6651 | *Confeccionamos peças sob medida,"
    " consulte-nos.*[cite: 11, 13]"
)

st.divider()


# Função para exibir PDF de forma compatível com os navegadores
def exibir_pdf(arquivo_pdf):
  try:
    with open(arquivo_pdf, "rb") as f:
      bytes_pdf = f.read()
      base64_pdf = base64.b64encode(bytes_pdf).decode("utf-8")

    # Exibição via tag object (melhor compatibilidade)
    pdf_display = f'<object data="data:application/pdf;base64,{base64_pdf}" type="application/pdf" width="100%" height="600px"><p>Seu navegador não suporta a exibição direta de PDF.</p></object>'
    st.markdown(pdf_display, unsafe_allow_html=True)

    # Botão de download direto logo abaixo
    st.download_button(
        label=f"📥 Baixar o arquivo {arquivo_pdf}",
        data=bytes_pdf,
        file_name=arquivo_pdf,
        mime="application/pdf",
    )
  except FileNotFoundError:
    st.error(
        f"Arquivo {arquivo_pdf} não encontrado no repositório. Verifique se o"
        " nome está exato."
    )


# Abas Principais
aba_cliente, aba_orcamento = st.tabs(
    ["👀 Catálogo e Medidas para o Cliente", "🧮 Gerador de Orçamentos"]
)

with aba_cliente:
  st.header("Guia Visual de Tamanhos e Medidas")
  st.write(
      "Selecione a categoria abaixo para visualizar o esquema oficial de"
      " tamanhos:"
  )

  escolha_tabela = st.selectbox(
      "Escolha a categoria de vestuário:",
      ["Camisetas Adultas", "Tamanhos Infantis", "Tamanhos Baby Look"],
  )

  st.markdown("---")

  if escolha_tabela == "Camisetas Adultas":
    st.subheader("👕 Tabela de Camisetas Adultas")
    st.markdown(
        "Consulte abaixo o documento oficial com as medidas detalhadas (PP ao"
        f" XGG)[cite: 7]:"
    )
    exibir_pdf("Tamanhos Camisetas-1.pdf")

  elif escolha_tabela == "Tamanhos Infantis":
    st.subheader("🧒 Tabela de Tamanhos Infantis")
    st.markdown(
        "Consulte abaixo o documento oficial com as medidas infantis (Tamanho"
        f" 1 ao 14)[cite: 8]:"
    )
    exibir_pdf("Tamanhos infantis.pdf")

  elif escolha_tabela == "Tamanhos Baby Look":
    st.subheader("👚 Tabela de Baby Look")
    st.markdown(
        "Consulte abaixo o documento oficial com as medidas de Baby Look (P ao"
        f" XG)[cite: 13]:"
    )
    exibir_pdf("Tamnhos babylook.pdf")

with aba_orcamento:
  st.header("Gerador de Orçamentos e Cotações")

  col_a, col_b = st.columns(2)

  with col_a:
    cliente_nome = st.text_input("Nome do Cliente / Empresa:")
    tecido_escolhido = st.selectbox(
        "Escolha o Tecido / Composição:", list(TABELA_TECIDOS.keys())
    )

  with col_b:
    condicao_pagamento = st.radio("Condição de Pagamento:", ["À Vista", "A Prazo"])
    quantidade = st.number_input(
        "Quantidade de Peças:", min_value=1, value=10, step=1
    )

  # Cálculo financeiro
  if condicao_pagamento == "À Vista":
    preco_unitario = TABELA_TECIDOS[tecido_escolhido]["avista"]
  else:
    preco_unitario = TABELA_TECIDOS[tecido_escolhido]["prazo"]

  valor_total = preco_unitario * quantidade

  st.divider()

  # Cartão de Resumo em destaque
  st.subheader("Resumo da Cotação")

  m1, m2, m3 = st.columns(3)
  m1.metric("Preço Unitário", f"R$ {preco_unitario:.2f}")
  m2.metric("Quantidade", f"{quantidade} un.")
  m3.metric("Valor Total", f"R$ {valor_total:.2f}")

  st.write(f"**Cliente:** {cliente_nome if cliente_nome else 'Cliente Geral'}")
  st.write(f"**Tecido Selecionado:** {tecido_escolhido}")
  st.write(f"**Condição:** {condicao_pagamento}")

  st.markdown("---")

  if st.button("Gerar Texto Formatado para WhatsApp"):
    texto_wpp = (
        f"*ORÇAMENTO - BENELLI CONFECÇÕES*\n"
        f"Olá *{cliente_nome if cliente_nome else 'Cliente'}*, segue a sua"
        f" cotação:\n\n• *Tecido:* {tecido_escolhido}\n• *Quantidade:* {quantidade}"
        f" peças\n• *Condição:* {condicao_pagamento}\n• *Valor Unitário:* R$"
        f" {preco_unitario:.2f}\n• *Valor Total:* *R$ {valor_total:.2f}*\n\nFicamos"
        " à disposição! Entre em contato pelo telefone (35) 98846-6651[cite: 11]."
    )
    st.success("Texto gerado com sucesso! Copie abaixo:")
    st.text_area("Mensagem pronta para envio:", texto_wpp, height=160)
