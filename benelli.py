import math
import streamlit as st

st.set_page_config(
    page_title="Benelli Confecções - Sistema de Orçamentos",
    layout="centered",
)

# --- CABEÇALHO COM LOGOTIPO ---
col_logo1, col_logo2, col_logo3 = st.columns([1, 2, 1])
with col_logo2:
  try:
    st.image("logo_benelli.png", use_container_width=True)
  except Exception:
    st.markdown(
        "<h2 style='text-align: center;'>Benelli Confecções</h2>",
        unsafe_allow_html=True,
    )

st.markdown(
    "<h4 style='text-align: center; color: #555;'>Sistema Integrado de"
    " Orçamentos</h4>",
    unsafe_allow_html=True,
)
st.markdown("---")

# TABELA OFICIAL DE TECIDOS (MARCELO)
TABELA_TECIDOS = {
    "M/M Cardada Branca (100% CO)": {
        "avista": 36.16,
        "aprazo": 36.90,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "M/M Cardada Escura (100% CO)": {
        "avista": 46.94,
        "aprazo": 47.90,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "M/M Penteada Branca (100% CO)": {
        "avista": 44.98,
        "aprazo": 45.90,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "M/M Penteada Clara (100% CO)": {
        "avista": 51.84,
        "aprazo": 52.90,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "M/M Penteada Media (100% CO)": {
        "avista": 53.80,
        "aprazo": 54.90,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "M/M Penteada Escura (100% CO)": {
        "avista": 55.66,
        "aprazo": 56.80,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "M/M Penteada Especial (Bandeira, Roxo, Royal, Vinho)": {
        "avista": 56.64,
        "aprazo": 57.80,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "M/M Penteada Mescla (88% CO 12% PES)": {
        "avista": 45.57,
        "aprazo": 46.50,
        "tipo": "padrao",
        "composicao": "misto",
    },
    "M/M Penteada Camuflada (100% CO)": {
        "avista": 74.48,
        "aprazo": 76.00,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "M/M PES Fiado Branca (100% PES)": {
        "avista": 30.48,
        "aprazo": 31.10,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "M/M PES Fiado Clara": {
        "avista": 32.24,
        "aprazo": 32.90,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "M/M PES Fiado Media": {
        "avista": 33.22,
        "aprazo": 33.90,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "M/M PES Fiado Escura": {
        "avista": 34.79,
        "aprazo": 35.50,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "M/M PES Fiado Especial": {
        "avista": 39.10,
        "aprazo": 39.90,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "M/M PES Fiado Mescla": {
        "avista": 31.85,
        "aprazo": 32.50,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "M/M Piquet Poliéster (Rende 4 pçs/kg)": {
        "avista": 30.48,
        "aprazo": 31.10,
        "tipo": "piquet_4",
        "composicao": "poliester",
    },
    "P.V. / Piquet de P.V. Branca": {
        "avista": 33.22,
        "aprazo": 33.90,
        "tipo": "piquet_4",
        "composicao": "misto",
    },
    "P.V. / Piquet de P.V. Clara": {
        "avista": 33.66,
        "aprazo": 34.35,
        "tipo": "piquet_4",
        "composicao": "misto",
    },
    "P.V. / Piquet de P.V. Media": {
        "avista": 36.16,
        "aprazo": 36.90,
        "tipo": "piquet_4",
        "composicao": "misto",
    },
    "P.V. / Piquet de P.V. Escura": {
        "avista": 42.04,
        "aprazo": 42.90,
        "tipo": "piquet_4",
        "composicao": "misto",
    },
    "P.V. / Piquet de P.V. Especial": {
        "avista": 44.44,
        "aprazo": 45.35,
        "tipo": "piquet_4",
        "composicao": "misto",
    },
    "P.V. / Piquet de P.V. Mescla": {
        "avista": 34.20,
        "aprazo": 34.90,
        "tipo": "piquet_4",
        "composicao": "misto",
    },
    "M/M Piquet 50/50% (Rende 3 pçs/kg)": {
        "avista": 41.06,
        "aprazo": 41.90,
        "tipo": "piquet_3",
        "composicao": "misto",
    },
    "M/M Piquet Claro (50/50)": {
        "avista": 42.04,
        "aprazo": 42.90,
        "tipo": "piquet_3",
        "composicao": "misto",
    },
    "M/M Piquet Medio (50/50)": {
        "avista": 45.96,
        "aprazo": 46.90,
        "tipo": "piquet_3",
        "composicao": "misto",
    },
    "M/M Piquet Escuro (50/50)": {
        "avista": 48.90,
        "aprazo": 49.90,
        "tipo": "piquet_3",
        "composicao": "misto",
    },
    "M/M Piquet Especial (50/50)": {
        "avista": 53.80,
        "aprazo": 54.90,
        "tipo": "piquet_3",
        "composicao": "misto",
    },
    "M/M Piquet Especial I Turquesa (50/50)": {
        "avista": 59.68,
        "aprazo": 60.90,
        "tipo": "piquet_3",
        "composicao": "misto",
    },
    "M/M Piquet Mescla (50/50)": {
        "avista": 47.92,
        "aprazo": 48.90,
        "tipo": "piquet_3",
        "composicao": "misto",
    },
    "M/M Dry Fit / Dry Sport Branco": {
        "avista": 37.14,
        "aprazo": 37.90,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "M/M Dry Fit / Dry Sport Escuro": {
        "avista": 41.65,
        "aprazo": 42.50,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "M/M Dry Fit / Dry Sport Especial": {
        "avista": 45.96,
        "aprazo": 46.90,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "Suedine 100% Algodão Branca": {
        "avista": 52.80,
        "aprazo": 53.90,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "Suedine 100% Algodão Cores": {
        "avista": 61.60,
        "aprazo": 62.90,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "Suedine 100% Algodão Estampada": {
        "avista": 68.50,
        "aprazo": 69.90,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "Moletom CIC P.A. Flanelado Branco": {
        "avista": 50.86,
        "aprazo": 51.90,
        "tipo": "moletom",
        "composicao": "misto",
    },
    "Moletom CIC P.A. Flanelado Cores": {
        "avista": 52.43,
        "aprazo": 53.50,
        "tipo": "moletom",
        "composicao": "misto",
    },
    "Moletom CIC P.A. Flanelado Mescla": {
        "avista": 45.47,
        "aprazo": 46.40,
        "tipo": "moletom",
        "composicao": "misto",
    },
    "Sarja Uniforte Santanense Claras": {
        "avista": 26.41,
        "aprazo": 26.95,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "Sarja Uniforte Santanense Cores": {
        "avista": 29.11,
        "aprazo": 29.70,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "Sarja Uniforte Santanense Escuras": {
        "avista": 29.89,
        "aprazo": 30.50,
        "tipo": "padrao",
        "composicao": "algodao",
    },
    "Tactel Microfibra Liso": {
        "avista": 22.50,
        "aprazo": 23.00,
        "tipo": "padrao",
        "composicao": "poliester",
    },
    "Oxford Poliéster": {
        "avista": 24.50,
        "aprazo": 25.00,
        "tipo": "padrao",
        "composicao": "poliester",
    },
}

st.subheader("📋 Parâmetros do Pedido")

tecido_nome = st.selectbox(
    "Escolha o Tecido / Cor:", list(TABELA_TECIDOS.keys())
)
cond = st.radio("Condição de Pagamento:", ["À Vista", "A Prazo"], horizontal=True)
cond_key = "avista" if cond == "À Vista" else "aprazo"

st.markdown("**Quantidades por Tamanho:**")
c1, c2, c3, c4 = st.columns(4)
with c1:
  pp = st.number_input("PP", min_value=0, value=0, step=1)
  p = st.number_input("P", min_value=0, value=0, step=1)
with c2:
  m = st.number_input("M", min_value=0, value=0, step=1)
  g = st.number_input("G", min_value=0, value=0, step=1)
with c3:
  gg = st.number_input("GG", min_value=0, value=0, step=1)
  xg = st.number_input("XG", min_value=0, value=0, step=1)
with c4:
  xgg = st.number_input("XGG", min_value=0, value=0, step=1)

d = {"PP": pp, "P": p, "M": m, "G": g, "GG": gg, "XG": xg, "XGG": xgg}
total_pecas = sum(d.values())

modelo_escolhido = st.selectbox(
    "Modelo (Custo Costura + Aviamentos):",
    [
        "Camiseta (R$ 5,00)",
        "Camisa Polo (R$ 8,00)",
        "Moletom Fechado (R$ 10,00)",
        "Moletom Aberto/Jaqueta c/ Zíper (R$ 21,00)",
    ],
)

est_escolhida = st.radio(
    "Modalidade de Estampa:",
    ["Nenhuma", "Silk Screen", "Digital", "DTF"],
    horizontal=True,
)

n_cores = 1
tipo_dig = "Localizada (Simples)"
larg, alt = 20.0, 25.0

if est_escolhida == "Silk Screen":
  n_cores = st.number_input(
      "Número de Cores (Silk):", min_value=1, value=1, step=1
  )
elif est_escolhida == "Digital":
  tipo_dig = st.selectbox(
      "Tipo Digital:",
      ["Localizada (Simples)", "Localizada (Frente e Costas)", "Total"],
  )
elif est_escolhida == "DTF":
  col_l, col_a = st.columns(2)
  with col_l:
    larg = st.number_input("Largura da Arte (cm):", min_value=1.0, value=20.0)
  with col_a:
    alt = st.number_input("Altura da Arte (cm):", min_value=1.0, value=25.0)

custo_extra = st.number_input(
    "Frete / Custos Extras (Total R$):", min_value=0.0, value=0.0, step=5.0
)

# Seletor de Margem de Lucro para o Cliente (25% a 70% de 5 em 5)
margem_lucro = st.selectbox(
    "Margem de Lucro para o Cliente (%):",
    options=list(range(25, 71, 5)),
    index=5,  # Padrão em 50% (índice 5)
)

st.markdown("---")

# --- PROCESSAMENTO DOS CÁLCULOS ---
dados_tec = TABELA_TECIDOS[tecido_nome]
preco_kg = dados_tec[cond_key]
tipo_tec = dados_tec["tipo"]
comp_tec = dados_tec["composicao"]

alerta_msg = ""
if est_escolhida == "Digital" and comp_tec != "poliester":
  alerta_msg = (
      "⚠️ ALERTA: A Impressão Digital só funciona em 100% Poliéster (ex: Dry"
      " Fit)!"
  )
  st.warning(alerta_msg)

if total_pecas > 0:
  # Tecido
  if tipo_tec == "piquet_4":
    kg_bruto = total_pecas / 4.0
  elif tipo_tec == "piquet_3":
    kg_bruto = total_pecas / 3.0
  elif tipo_tec == "moletom":
    pmg = d["P"] + d["M"] + d["G"]
    outros = d["PP"] + d["GG"] + d["XG"] + d["XGG"]
    kg_bruto = (pmg * 0.8) + (outros * 1.1)
  else:
    pp_p_m_g = d["PP"] + d["P"] + d["M"] + d["G"]
    gg = d["GG"]
    xg_xgg = d["XG"] + d["XGG"]
    kg_bruto = (pp_p_m_g / 4.0) + (gg / 3.0) + (xg_xgg / 2.0)

  kg_comprado = math.ceil(kg_bruto * 2) / 2.0
  if kg_comprado < 1.0:
    kg_comprado = 1.0

  custo_tecido_total = kg_comprado * preco_kg

  # Costura + Aviamentos
  if "Polo" in modelo_escolhido:
    custo_unit_costura = 8.00
  elif "Moletom Fechado" in modelo_escolhido:
    custo_unit_costura = 10.00
  elif "Moletom Aberto" in modelo_escolhido:
    custo_unit_costura = 21.00
  else:
    custo_unit_costura = 5.00

  custo_costura_total = custo_unit_costura * total_pecas

  # Estampa
  custo_estampa_total = 0.0
  detalhes_estampa_str = "Sem estampa"

  if est_escolhida == "Silk Screen":
    qtd_cobranca_silk = max(total_pecas, 10)
    custo_por_peca_silk = 1.50 + (n_cores * 0.70)
    custo_estampa_total = custo_por_peca_silk * qtd_cobranca_silk
    detalhes_estampa_str = (
        f"Silk Screen ({n_cores} cor(es)): R$ {custo_por_peca_silk:.2f}/pç"
        f" (Lote mín. cobrado: {qtd_cobranca_silk} pçs)"
    )
  elif est_escolhida == "Digital":
    if "Frente e Costas" in tipo_dig or "Total" in tipo_dig:
      custo_unit_dig = 25.00
      detalhes_estampa_str = "Impressão Digital Total / Frente e Costas"
    else:
      custo_unit_dig = 8.00
      detalhes_estampa_str = "Impressão Digital Localizada"
    custo_estampa_total = custo_unit_dig * total_pecas
  elif est_escolhida == "DTF":
    area_arte_peca = larg * alt
    area_total_arte = area_arte_peca * total_pecas
    meias_folhas_necessarias = math.ceil(area_total_arte / 2500.0)
    if meias_folhas_necessarias < 1:
      meias_folhas_necessarias = 1
    custo_estampa_total = meias_folhas_necessarias * 25.00
    detalhes_estampa_str = (
        f"DTF ({larg}x{alt}cm por peça): {meias_folhas_necessarias} meia(s)"
        " folha(s) de 50x50cm"
    )

  # Custo de Produção Total e Unitário (Puro, sem margem - para o Marcelo)
  custo_geral_total = (
      custo_tecido_total + custo_costura_total + custo_estampa_total + custo_extra
  )
  custo_unitario_final = custo_geral_total / total_pecas

  # Valor de Venda com Margem de Lucro (Aplicado para o Cliente)
  fator_lucro = 1 + (margem_lucro / 100.0)
  venda_geral_total = custo_geral_total * fator_lucro
  venda_unitario_final = custo_unitario_final * fator_lucro

  grade_str = ", ".join([f"{t}: {v}" for t, v in d.items() if v > 0])

  st.subheader("📊 Resultados e Textos de Saída")

  # Texto do Marcelo (Custo puro de produção)
  texto_m = f"""=== PROVA REAL (PARA O MARCELO) ===
Quantidade: {total_pecas} peça(s) [{grade_str}]
Modelo / Costura: {modelo_escolhido} (R$ {custo_unit_costura:.2f}/pç)
- Custo Costura + Aviamentos: R$ {custo_costura_total:.2f}

Tecido: {tecido_nome} ({cond.upper()})
- Preço do Quilo: R$ {preco_kg:.2f}
- Tecido Bruto: {kg_bruto:.2f} kg | Faturado (Fábrica): {kg_comprado:.1f} kg
- Custo Total do Tecido: R$ {custo_tecido_total:.2f}

Estampa: {detalhes_estampa_str}
- Custo Total da Estampa: R$ {custo_estampa_total:.2f}

Frete / Custos Extras: R$ {custo_extra:.2f}
---------------------------------------------
CUSTO GERAL DE PRODUÇÃO: R$ {custo_geral_total:.2f}
Custo Real Unitário: R$ {custo_unitario_final:.2f} / peça
{alerta_msg}
"""
  st.text_area("Texto para o Marcelo (Prova Real - Custo)", texto_m, height=280)

  # Texto do Cliente (Com a margem de lucro aplicada)
  texto_c = f"""=== ORÇAMENTO COMERCIAL ===
Quantidade: {total_pecas} peça(s)
Item: {modelo_escolhido.split('(')[0].strip()} em {tecido_nome} com {est_escolhida.lower()}

VALOR TOTAL DO PEDIDO: R$ {venda_geral_total:.2f}
VALOR POR UNIDADE: R$ {venda_unitario_final:.2f} cada
"""
  st.text_area(
      f"Texto para o Cliente (Com {margem_lucro}% de Lucro)", texto_c, height=180
  )
else:
  st.info(
      "👆 Preencha as quantidades na grade de tamanhos acima para gerar os"
      " orçamentos."
  )
