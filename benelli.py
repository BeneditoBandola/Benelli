import streamlit as st

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Benelli Confecções - Orçamentos e Medidas",
    page_icon="👕",
    layout="wide",
)

# Estilo visual personalizado (CSS)
st.markdown("""
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
""", unsafe_allow_html=True)

# Tabela de preços oficial
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

# Cabeçalho com link para o Instagram
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("👕 Benelli Confecções")
    st.markdown("##### *Sistema Profissional de Orçamentos e Consulta de Medidas*")
    st.info("📞 **Contato direto:** (35) 98846-6651 | *Confeccionamos peças sob medida, consulte-nos.*")
with col_head2:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<a href="https://www.instagram.com/benelliconfeccoes/" target="_blank" style="background-color: #E1306C; color: white; padding: 10px 15px; border-radius: 6px; text-decoration: none; font-weight: bold; display: inline-block; text-align: center; width: 100%;">📸 Siga no Instagram</a>',
        unsafe_allow_html=True
    )

st.divider()

# Abas Principais
aba_cliente, aba_orcamento = st.tabs(["👀 Catálogo e Medidas para o Cliente", "🧮 Gerador de Orçamentos"])

with aba_cliente:
    st.header("Guia Visual de Tamanhos e Medidas")
    st.write("Selecione a categoria abaixo para visualizar o esquema oficial diretamente na tela:")

    escolha_tabela = st.selectbox(
        "Escolha a categoria de vestuário:",
        ["Camisetas Adultas", "Tamanhos Infantis", "Tamanhos Baby Look"]
    )

    st.markdown("---")

    if escolha_tabela == "Camisetas Adultas":
        st.subheader("👕 Tabela de Camisetas Adultas")
        st.image("tamanhos camisetas.png", caption="Esquema de Medidas - Camisetas Adultas", use_container_width=True)

    elif escolha_tabela == "Tamanhos Infantis":
        st.subheader("🧒 Tabela de Tamanhos Infantis")
        st.image("tamanhos infantil.png", caption="Esquema de Medidas - Infantil", use_container_width=True)

    elif escolha_tabela == "Tamanhos Baby Look":
        st.subheader("👚 Tabela de Baby Look")
        st.image("baby look.png", caption="Esquema de Medidas - Baby Look", use_container_width=True)

with aba_orcamento:
    st.header("Gerador de Orçamentos e Cotações")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        cliente_nome = st.text_input("Nome do Cliente / Empresa:")
        tecido_escolhido = st.selectbox("Escolha o Tecido / Composição:", list(TABELA_TECIDOS.keys()))
        condicao_pagamento = st.radio("Condição de Pagamento:", ["À Vista", "A Prazo"])

    with col_b:
        st.subheader("Quantidades por Tamanho")
        tipo_grade = st.selectbox("Selecione a Grade:", ["Adulto (PP ao XGG)", "Infantil (1 ao 14)", "Baby Look (P ao XG)"])
        
        quantidades_tamanhos = {}
        
        if tipo_grade == "Adulto (PP ao XGG)":
            tamanhos_lista = ["PP", "P", "M", "G", "GG", "XG", "XGG"]
        elif tipo_grade == "Infantil (1 ao 14)":
            tamanhos_lista = ["Tam 1", "Tam 2", "Tam 3", "Tam 4", "Tam 6", "Tam 8", "Tam 10", "Tam 12", "Tam 14"]
        else:
            tamanhos_lista = ["P", "M", "G", "GG", "XG"]
            
        # Criando campos de número para cada tamanho lado a lado em colunas
        cols_tam = st.columns(min(len(tamanhos_lista), 4))
        for i, tam in enumerate(tamanhos_lista):
            with cols_tam[i % len(cols_tam)]:
                quantidades_tamanhos[tam] = st.number_input(f"Tam {tam}", min_value=0, value=0, step=1, key=f"tam_{tam}")

    # Cálculo financeiro total
    quantidade_total = sum(quantidades_tamanhos.values())
    
    if condicao_pagamento == "À Vista":
        preco_unitario = TABELA_TECIDOS[tecido_escolhido]["avista"]
    else:
        preco_unitario = TABELA_TECIDOS[tecido_escolhido]["prazo"]

    valor_total = preco_unitario * quantidade_total

    st.divider()
    
    st.subheader("Resumo da Cotação")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Preço Unitário", f"R$ {preco_unitario:.2f}")
    m2.metric("Qtd. Total", f"{quantidade_total} un.")
    m3.metric("Valor Total", f"R$ {valor_total:.2f}")

    st.write(f"**Cliente:** {cliente_nome if cliente_nome else 'Cliente Geral'}")
    st.write(f"**Tecido Selecionado:** {tecido_escolhido}")
    st.write(f"**Condição:** {condicao_pagamento}")
    
    # Exibir detalhamento por tamanho se houver quantidade
    if quantidade_total > 0:
        detalhe_tamanhos_str = ", ".join([f"{qtd}x {tam}" for tam, qtd in quantidades_tamanhos.items() if qtd > 0])
        st.write(f"**Distribuição de Tamanhos:** {detalhe_tamanhos_str}")

    st.markdown("---")

    if st.button("Gerar Texto Formatado para WhatsApp"):
        detalhe_wpp = "\n".join([f"  - {tam}: {qtd} peça(s)" for tam, qtd in quantidades_tamanhos.items() if qtd > 0])
        
        texto_wpp = (
            f"*ORÇAMENTO - BENELLI CONFECÇÕES*\n"
            f"Olá *{cliente_nome if cliente_nome else 'Cliente'}*, segue a sua cotação:\n\n"
            f"• *Tecido:* {tecido_escolhido}\n"
            f"• *Quantidade Total:* {quantidade_total} peças\n"
            f"• *Distribuição de Tamanhos:*\n{detalhe_wpp}\n\n"
            f"• *Condição:* {condicao_pagamento}\n"
            f"• *Valor Unitário:* R$ {preco_unitario:.2f}\n"
            f"• *Valor Total:* *R$ {valor_total:.2f}*\n\n"
            f"Ficamos à disposição! Conheça nosso trabalho no Instagram: https://www.instagram.com/benelliconfeccoes/\n"
            f"Entre em contato pelo telefone (35) 98846-6651."
        )
        st.success("Texto gerado com sucesso! Copie abaixo:")
        st.text_area("Mensagem pronta para envio:", texto_wpp, height=200)
