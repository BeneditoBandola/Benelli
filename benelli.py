from io import BytesIO
import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

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


# Função auxiliar para formatar valores no padrão brasileiro (R$ 0,00)
def formata_real(valor):
  return (
      f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
  )


# Tabela de preços oficial e Guia de Tecidos
TABELA_TECIDOS = {
    "Meia Malha Cardada - Branca": {
        "avista": 36.16,
        "prazo": 36.90,
        "desc": (
            "Feita com fio 100% algodão cardado. É uma opção mais econômica,"
            " com toque macio e bom caimento, ideal para peças promocionais e"
            " uso diário."
        ),
        "beneficios": "Excelente custo-benefício, confortável e versátil.",
        "indicacao": "Camisetas promocionais, eventos e fardamentos básicos.",
    },
    "Meia Malha Cardada - Escura": {
        "avista": 46.94,
        "prazo": 47.90,
        "desc": (
            "Algodão cardado com tingimento em tons escuros. Mantém a"
            " resistência e o conforto característicos do algodão."
        ),
        "beneficios": "Boa durabilidade e cores sólidas.",
        "indicacao": "Uniformes operacionais e vestuário casual.",
    },
    "Meia Malha Penteada - Branca": {
        "avista": 44.98,
        "prazo": 45.90,
        "desc": (
            "Fio 100% algodão submetido ao processo de penteagem, que elimina"
            " fibras curtas. O resultado é um tecido mais limpo, macio e com"
            " maior durabilidade."
        ),
        "beneficios": (
            "Toque superior, não forma pilling facilmente, excelente"
            " acabamento."
        ),
        "indicacao": "Moda urbana, marcas próprias e camisetas de alto padrão.",
    },
    "Meia Malha Penteada - Clara": {
        "avista": 51.84,
        "prazo": 52.90,
        "desc": (
            "Algodão penteado em tons claros. Toque suave e excelente absorção."
        ),
        "beneficios": "Conforto térmico elevado e toque aveludado.",
        "indicacao": "Linha casual e vestuário diário refinado.",
    },
    "Meia Malha Penteada - Média": {
        "avista": 53.80,
        "prazo": 54.90,
        "desc": "Malha penteada de gramatura ideal para meia-estação.",
        "beneficios": "Equilíbrio perfeito entre leveza e estrutura.",
        "indicacao": "Camisetas premium e uniformes corporativos.",
    },
    "Meia Malha Penteada - Escura": {
        "avista": 55.66,
        "prazo": 56.80,
        "desc": "Algodão penteado escuro com tingimento de alta fixação.",
        "beneficios": "Cores vivas por mais tempo e toque extremamente macio.",
        "indicacao": "Camisetas de marca e coleções exclusivas.",
    },
    "Meia Malha Poliéster Fiado - Branca": {
        "avista": 30.48,
        "prazo": 31.10,
        "desc": (
            "Tecido 100% poliéster. Seca muito rápido, não amassa e tem alta"
            " resistência."
        ),
        "beneficios": "Não encolhe, não precisa passar e tem secagem rápida.",
        "indicacao": "Eventos esportivos, abadás e campanhas.",
    },
    "Meia Malha Poliéster Fiado - Escura": {
        "avista": 34.79,
        "prazo": 35.50,
        "desc": "Versão em poliéster fiado com cores escuras.",
        "beneficios": "Praticidade no dia a dia e alta durabilidade.",
        "indicacao": "Uniformes leves e peças promocionais.",
    },
    "Meia Malha Dry Fit / Dry Sport - Branca": {
        "avista": 37.14,
        "prazo": 37.90,
        "desc": (
            "Tecido tecnológico desenvolvido para facilitar a evaporação do"
            " suor."
        ),
        "beneficios": (
            "Excelente respirabilidade e conforto térmico durante"
            " exercícios."
        ),
        "indicacao": "Uniformes esportivos, academias e corridas.",
    },
    "Meia Malha Dry Fit / Dry Sport - Escura": {
        "avista": 41.65,
        "prazo": 42.50,
        "desc": "Malha Dry Fit em tons escuros com excelente caimento esportivo.",
        "beneficios": "Leveza, absorção de suor e toque gelado.",
        "indicacao": "Camisas de equipes de futebol e vestuário fitness.",
    },
    "Moletom Flanelado Cores": {
        "avista": 52.43,
        "prazo": 53.50,
        "desc": (
            "Composição P.A. (50% algodão, 50% poliéster) flanelado por dentro."
            " Proporciona excelente aquecimento nos dias frios."
        ),
        "beneficios": "Quente, macio, confortável e resistente.",
        "indicacao": "Casacos, moletons de inverno e uniformes escolares.",
    },
    "Suedine P.A. Cores": {
        "avista": 53.80,
        "prazo": 54.90,
        "desc": (
            "Malha encorpada com toque semelhante à pele, muito usada na linha"
            " infantil e de alta qualidade."
        ),
        "beneficios": (
            "Extremamente macio, seguro para peles sensíveis e estruturado."
        ),
        "indicacao": "Moda infantil e peças de inverno leve.",
    },
}

# Cabeçalho com link para o Instagram
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
  st.title("👕 Benelli Confecções")
  st.markdown("##### *Sistema Profissional de Orçamentos e Consulta de Medidas*")
  st.info(
      "📞 **Contato direto:** (35) 98846-6651 | *Confeccionamos peças sob medida,"
      " consulte-nos.*"
  )
with col_head2:
  st.markdown("<br>", unsafe_allow_html=True)
  st.markdown(
      '<a href="https://www.instagram.com/benelliconfeccoes/" target="_blank"'
      ' style="background-color: #E1306C; color: white; padding: 10px 15px;'
      " border-radius: 6px; text-decoration: none; font-weight: bold; display:"
      ' inline-block; text-align: center; width: 100%;">📸 Siga no Instagram</a>',
      unsafe_allow_html=True,
  )

st.divider()

# Abas Principais
aba_cliente, aba_tecidos, aba_orcamento = st.tabs([
    "👀 Catálogo e Medidas",
    "🧵 Guia Inteligente de Tecidos",
    "🧮 Gerador de Orçamentos",
])

with aba_cliente:
  st.header("Guia Visual de Tamanhos e Medidas")
  st.write(
      "Selecione a categoria abaixo para visualizar o esquema oficial"
      " diretamente na tela:"
  )

  escolha_tabela = st.selectbox(
      "Escolha a categoria de vestuário:",
      ["Camisetas Adultas", "Tamanhos Infantis", "Tamanhos Baby Look"],
  )

  st.markdown("---")

  if escolha_tabela == "Camisetas Adultas":
    st.subheader("👕 Tabela de Camisetas Adultas")
    st.image(
        "tamanhos camisetas.png",
        caption="Esquema de Medidas - Camisetas Adultas",
        use_container_width=True,
    )

  elif escolha_tabela == "Tamanhos Infantis":
    st.subheader("🧒 Tabela de Tamanhos Infantis")
    st.image(
        "tamanhos infantil.png",
        caption="Esquema de Medidas - Infantil",
        use_container_width=True,
    )

  elif escolha_tabela == "Tamanhos Baby Look":
    st.subheader("👚 Tabela de Baby Look")
    st.image(
        "baby look.png",
        caption="Esquema de Medidas - Baby Look",
        use_container_width=True,
    )

with aba_tecidos:
  st.header("🧵 Guia Inteligente de Tecidos Benelli")
  st.write(
      "Conheça as características, benefícios e indicações de cada material"
      " para ajudar na sua escolha:"
  )

  for nome_tecido, info in TABELA_TECIDOS.items():
    with st.expander(f"📌 {nome_tecido}"):
      st.write(f"**Descrição:** {info['desc']}")
      st.write(f"✨ **Benefícios:** {info['beneficios']}")
      st.write(f"🎯 **Ideal para:** {info['indicacao']}")
      st.write(
          f"💰 **Preço (À Vista):** {formata_real(info['avista'])} | **A"
          f" Prazo:** {formata_real(info['prazo'])}"
      )

with aba_orcamento:
  st.header("Gerador de Orçamentos e Cotações")

  col_a, col_b = st.columns(2)

  with col_a:
    cliente_nome = st.text_input("Nome do Cliente / Empresa:")
    tecido_escolhido = st.selectbox(
        "Escolha o Tecido / Composição:", list(TABELA_TECIDOS.keys())
    )
    condicao_pagamento = st.radio("Condição de Pagamento:", ["À Vista", "A Prazo"])

  with col_b:
    st.subheader("Quantidades por Tamanho")
    tipo_grade = st.selectbox(
        "Selecione a Grade:",
        ["Adulto (PP ao XGG)", "Infantil (1 ao 14)", "Baby Look (P ao XG)"],
    )

    quantidades_tamanhos = {}

    if tipo_grade == "Adulto (PP ao XGG)":
      tamanhos_lista = ["PP", "P", "M", "G", "GG", "XG", "XGG"]
    elif tipo_grade == "Infantil (1 ao 14)":
      tamanhos_lista = [
          "Tam 1",
          "Tam 2",
          "Tam 3",
          "Tam 4",
          "Tam 6",
          "Tam 8",
          "Tam 10",
          "Tam 12",
          "Tam 14",
      ]
    else:
      tamanhos_lista = ["P", "M", "G", "GG", "XG"]

    cols_tam = st.columns(min(len(tamanhos_lista), 4))
    for i, tam in enumerate(tamanhos_lista):
      with cols_tam[i % len(cols_tam)]:
        quantidades_tamanhos[tam] = st.number_input(
            f"Tam {tam}", min_value=0, value=0, step=1, key=f"tam_{tam}"
        )

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
  m1.metric("Preço Unitário", formata_real(preco_unitario))
  m2.metric("Qtd. Total", f"{quantidade_total} un.")
  m3.metric("Valor Total", formata_real(valor_total))

  st.write(f"**Cliente:** {cliente_nome if cliente_nome else 'Cliente Geral'}")
  st.write(f"**Tecido Selecionado:** {tecido_escolhido}")
  st.write(f"**Condição:** {condicao_pagamento}")

  detalhe_tamanhos_str = ", ".join(
      [f"{qtd}x {tam}" for tam, qtd in quantidades_tamanhos.items() if qtd > 0]
  )
  if quantidade_total > 0:
    st.write(f"**Distribuição de Tamanhos:** {detalhe_tamanhos_str}")

  st.markdown("---")


  # Função para gerar o PDF formatado com ReportLab no padrão brasileiro
  def gerar_pdf_orcamento():
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    largura, altura = A4

    # Cabeçalho do PDF
    c.setFillColorRGB(0.1, 0.2, 0.3)
    c.rect(0, altura - 80, largura, 80, fill=1, stroke=0)

    c.setFillColorRGB(1, 1, 1)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(40, altura - 45, "BENELLI CONFECÇÕES")
    c.setFont("Helvetica", 12)
    c.drawString(
        40, altura - 65, "Orçamento Oficial - Contato: (35) 98846-6651"
    )

    # Dados do Cliente
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(
        40,
        altura - 120,
        f"Cliente: {cliente_nome if cliente_nome else 'Cliente Geral'}",
    )
    c.setFont("Helvetica", 11)
    c.drawString(
        40, altura - 145, f"Tecido / Composição: {tecido_escolhido}"
    )
    c.drawString(40, altura - 165, f"Condição de Pagamento: {condicao_pagamento}")
    c.drawString(
        40, altura - 185, f"Quantidade Total: {quantidade_total} peças"
    )

    # Detalhe dos Tamanhos
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, altura - 220, "Distribuição por Tamanho:")
    c.setFont("Helvetica", 11)
    y_pos = altura - 245
    for tam, qtd in quantidades_tamanhos.items():
      if qtd > 0:
        c.drawString(60, y_pos, f"• Tamanho {tam}: {qtd} unidade(s)")
        y_pos -= 20

    # Valores Finais
    y_pos -= 20
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.line(40, y_pos, largura - 40, y_pos)

    y_pos -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(
        40, y_pos, f"Preço Unitário: {formata_real(preco_unitario)}"
    )
    c.setFont("Helvetica-Bold", 16)
    c.setFillColorRGB(0.15, 0.5, 0.2)
    c.drawString(
        40, y_pos - 30, f"VALOR TOTAL: {formata_real(valor_total)}"
    )

    # Rodapé
    c.setFillColorRGB(0.4, 0.4, 0.4)
    c.setFont("Helvetica", 9)
    c.drawString(
        40,
        50,
        "Visite nosso Instagram: https://www.instagram.com/benelliconfeccoes/",
    )
    c.drawString(
        40, 35, "Benelli Confecções - Confeccionamos peças sob medida."
    )

    c.save()
    buffer.seek(0)
    return buffer


  # Botões de Ação lado a lado
  col_btn1, col_btn2 = st.columns(2)

  with col_btn1:
    if st.button("Gerar Texto para WhatsApp"):
      detalhe_wpp = "\n".join([
          f"  - {tam}: {qtd} peça(s)"
          for tam, qtd in quantidades_tamanhos.items()
          if qtd > 0
      ])
      texto_wpp = (
          f"*ORÇAMENTO - BENELLI CONFECÇÕES*\nOlá"
          f" *{cliente_nome if cliente_nome else 'Cliente'}*, segue a sua"
          f" cotação:\n\n• *Tecido:* {tecido_escolhido}\n• *Quantidade Total:*"
          f" {quantidade_total} peças\n• *Distribuição de"
          f" Tamanhos:*\n{detalhe_wpp}\n\n• *Condição:* {condicao_pagamento}\n•"
          f" *Valor Unitário:* {formata_real(preco_unitario)}\n• *Valor Total:*"
          f" *{formata_real(valor_total)}*\n\nFicamos à disposição! Conheça"
          " nosso trabalho no Instagram:"
          " https://www.instagram.com/benelliconfeccoes/\nEntre em contato pelo"
          " telefone (35) 98846-6651."
      )
      st.success("Texto gerado com sucesso!")
      st.text_area("Mensagem pronta para envio:", texto_wpp, height=180)

  with col_btn2:
    if quantidade_total > 0:
      pdf_buffer = gerar_pdf_orcamento()
      st.download_button(
          label="📥 Baixar Orçamento em PDF",
          data=pdf_buffer,
          file_name=(
              f"Orcamento_Benelli_{cliente_nome.replace(' ', '_') if cliente_nome else 'Cliente'}.pdf"
          ),
          mime="application/pdf",
      )
    else:
      st.warning(
          "Adicione ao menos 1 peça nos tamanhos para habilitar o PDF."
      )
