import math
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

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


class AppBenelliCompletoFinal(ctk.CTk):

  def __init__(self):
    super().__init__()
    self.title(
        "Benelli Confecções - Sistema Integrado de Orçamento Completo"
    )
    self.geometry("1150x800")
    self.resizable(False, False)

    # Título
    ctk.CTkLabel(
        self,
        text="Gerador de Orçamento - Benelli Confecções",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(pady=10)

    # Frame Principal
    self.frame_main = ctk.CTkFrame(self)
    self.frame_main.pack(padx=15, pady=5, fill="both", expand=True)

    # Coluna Esquerda (Entradas)
    self.col_esq = ctk.CTkFrame(self.frame_main, fg_color="transparent")
    self.col_esq.pack(
        side="left", fill="both", expand=True, padx=10, pady=10
    )

    # Tecido
    ctk.CTkLabel(self.col_esq, text="Escolha o Tecido / Cor:").pack(
        anchor="w", pady=(2, 0)
    )
    lista_tec = list(TABELA_TECIDOS.keys())
    self.combo_tecido = ctk.CTkComboBox(
        self.col_esq, values=lista_tec, width=380, command=self.calcular
    )
    self.combo_tecido.pack(anchor="w", pady=(0, 5))
    self.combo_tecido.set(lista_tec[0])

    # Condição Pagamento
    ctk.CTkLabel(self.col_esq, text="Condição de Pagamento:").pack(
        anchor="w", pady=(2, 0)
    )
    self.var_cond = ctk.StringVar(value="avista")
    f_cond = ctk.CTkFrame(self.col_esq, fg_color="transparent")
    f_cond.pack(anchor="w", pady=(0, 5))
    ctk.CTkRadioButton(
        f_cond,
        text="À Vista",
        variable=self.var_cond,
        value="avista",
        command=self.calcular,
    ).pack(side="left", padx=(0, 15))
    ctk.CTkRadioButton(
        f_cond,
        text="A Prazo",
        variable=self.var_cond,
        value="aprazo",
        command=self.calcular,
    ).pack(side="left")

    # Grade de Tamanhos
    ctk.CTkLabel(
        self.col_esq,
        text="Quantidades por Tamanho:",
        font=ctk.CTkFont(weight="bold"),
    ).pack(anchor="w", pady=(5, 2))
    self.entries_tam = {}
    f_grade_box = ctk.CTkFrame(self.col_esq)
    f_grade_box.pack(fill="x", pady=2)

    for tam in ["PP", "P", "M", "G", "GG", "XG", "XGG"]:
      subf = ctk.CTkFrame(f_grade_box, fg_color="transparent")
      subf.pack(side="left", padx=3, pady=5)
      ctk.CTkLabel(subf, text=tam, font=ctk.CTkFont(size=11)).pack()
      ent = ctk.CTkEntry(subf, width=38)
      ent.pack()
      ent.insert(0, "0")
      ent.bind("<KeyRelease>", self.calcular)
      self.entries_tam[tam] = ent

    # Tipo de Peça / Costura + Aviamentos
    ctk.CTkLabel(
        self.col_esq,
        text="Modelo (Custo Costura + Aviamentos):",
        font=ctk.CTkFont(weight="bold"),
    ).pack(anchor="w", pady=(10, 2))
    self.var_modelo = ctk.StringVar(value="Camiseta (R$ 5,00)")
    self.combo_modelo = ctk.CTkComboBox(
        self.col_esq,
        values=[
            "Camiseta (R$ 5,00)",
            "Camisa Polo (R$ 8,00)",
            "Moletom Fechado (R$ 10,00)",
            "Moletom Aberto/Jaqueta c/ Zíper (R$ 21,00)",
        ],
        variable=self.var_modelo,
        width=380,
        command=self.calcular,
    )
    self.combo_modelo.pack(anchor="w", pady=(0, 5))

    # Tipo de Estampa
    ctk.CTkLabel(
        self.col_esq,
        text="Modalidade de Estampa:",
        font=ctk.CTkFont(weight="bold"),
    ).pack(anchor="w", pady=(10, 2))
    self.var_estampa = ctk.StringVar(value="Nenhuma")
    f_est = ctk.CTkFrame(self.col_esq, fg_color="transparent")
    f_est.pack(anchor="w", pady=(0, 5))

    for est in ["Nenhuma", "Silk Screen", "Digital", "DTF"]:
      ctk.CTkRadioButton(
          f_est,
          text=est,
          variable=self.var_estampa,
          value=est,
          command=self.toggle_estampa_options,
      ).pack(side="left", padx=(0, 10))

    # Frame de Opções Dinâmicas de Estampa
    self.frame_opcoes_est = ctk.CTkFrame(self.col_esq)
    self.frame_opcoes_est.pack(fill="x", pady=5, padx=2)

    # Sub-opções Silk Screen
    self.f_silk = ctk.CTkFrame(self.frame_opcoes_est, fg_color="transparent")
    ctk.CTkLabel(self.f_silk, text="Nº Cores (Silk):").pack(side="left", padx=5)
    self.ent_cores_silk = ctk.CTkEntry(self.f_silk, width=50)
    self.ent_cores_silk.pack(side="left", padx=5)
    self.ent_cores_silk.insert(0, "1")
    self.ent_cores_silk.bind("<KeyRelease>", self.calcular)

    # Sub-opções Digital
    self.f_dig = ctk.CTkFrame(self.frame_opcoes_est, fg_color="transparent")
    ctk.CTkLabel(self.f_dig, text="Tipo Digital:").pack(side="left", padx=5)
    self.var_dig_tipo = ctk.StringVar(value="Localizada")
    self.combo_dig = ctk.CTkComboBox(
        self.f_dig,
        values=["Localizada (Simples)", "Localizada (Frente e Costas)", "Total"],
        variable=self.var_dig_tipo,
        width=180,
        command=self.calcular,
    )
    self.combo_dig.pack(side="left", padx=5)

    # Sub-opções DTF
    self.f_dtf = ctk.CTkFrame(self.frame_opcoes_est, fg_color="transparent")
    ctk.CTkLabel(self.f_dtf, text="Medida Arte DTF (Larg x Alt em cm):").pack(
        anchor="w", padx=5
    )
    f_dtf_dim = ctk.CTkFrame(self.f_dtf, fg_color="transparent")
    f_dtf_dim.pack(anchor="w", padx=5, pady=2)
    ctk.CTkLabel(f_dtf_dim, text="Larg:").pack(side="left")
    self.ent_dtf_larg = ctk.CTkEntry(f_dtf_dim, width=50)
    self.ent_dtf_larg.pack(side="left", padx=(2, 10))
    self.ent_dtf_larg.insert(0, "20")
    self.ent_dtf_larg.bind("<KeyRelease>", self.calcular)

    ctk.CTkLabel(f_dtf_dim, text="Alt:").pack(side="left")
    self.ent_dtf_alt = ctk.CTkEntry(f_dtf_dim, width=50)
    self.ent_dtf_alt.pack(side="left", padx=(2, 0))
    self.ent_dtf_alt.insert(0, "25")
    self.ent_dtf_alt.bind("<KeyRelease>", self.calcular)

    # Campo de Frete / Custos Extras
    f_extra = ctk.CTkFrame(self.col_esq, fg_color="transparent")
    f_extra.pack(fill="x", pady=(10, 2))
    ctk.CTkLabel(
        f_extra,
        text="Frete / Custos Extras (Total R$):",
        font=ctk.CTkFont(weight="bold"),
    ).pack(side="left", padx=5)
    self.ent_frete = ctk.CTkEntry(f_extra, width=100)
    self.ent_frete.pack(side="left", padx=5)
    self.ent_frete.insert(0, "0.00")
    self.ent_frete.bind("<KeyRelease>", self.calcular)

    # Alerta de Compatibilidade / Validação
    self.label_alerta = ctk.CTkLabel(
        self.col_esq, text="", text_color="#FF474C", font=ctk.CTkFont(size=12)
    )
    self.label_alerta.pack(anchor="w", pady=2)

    # Coluna Direita (Saídas de Texto)
    self.col_dir = ctk.CTkFrame(self.frame_main)
    self.col_dir.pack(
        side="right", fill="both", expand=True, padx=10, pady=10
    )

    ctk.CTkLabel(
        self.col_dir,
        text="TEXTO PARA O MARCELO (PROVA REAL)",
        font=ctk.CTkFont(size=12, weight="bold"),
    ).pack(pady=(5, 2))
    self.txt_marcelo = ctk.CTkTextbox(
        self.col_dir, width=450, height=330, font=ctk.CTkFont(size=11)
    )
    self.txt_marcelo.pack(pady=(0, 10))

    ctk.CTkLabel(
        self.col_dir,
        text="TEXTO PARA O CLIENTE (APENAS VALORES)",
        font=ctk.CTkFont(size=12, weight="bold"),
    ).pack(pady=(2, 2))
    self.txt_cliente = ctk.CTkTextbox(
        self.col_dir, width=450, height=240, font=ctk.CTkFont(size=11)
    )
    self.txt_cliente.pack(pady=(0, 5))

    self.toggle_estampa_options()
    self.calcular()

  def toggle_estampa_options(self):
    for w in self.frame_opcoes_est.winfo_children():
      w.pack_forget()
    est = self.var_estampa.get()
    if est == "Silk Screen":
      self.f_silk.pack(fill="x", padx=5, pady=5)
    elif est == "Digital":
      self.f_dig.pack(fill="x", padx=5, pady=5)
    elif est == "DTF":
      self.f_dtf.pack(fill="x", padx=5, pady=5)
    self.calcular()

  def calcular(self, event=None):
    try:
      d = {t: int(e.get().strip() or 0) for t, e in self.entries_tam.items()}
    except ValueError:
      return

    total_pecas = sum(d.values())
    tecido_nome = self.combo_tecido.get()
    dados_tec = TABELA_TECIDOS[tecido_nome]
    cond = self.var_cond.get()
    preco_kg = dados_tec[cond]
    tipo_tec = dados_tec["tipo"]
    comp_tec = dados_tec["composicao"]

    # 1. Validação de Compatibilidade de Estampa
    alerta_msg = ""
    est_escolhida = self.var_estampa.get()
    if est_escolhida == "Digital" and comp_tec != "poliester":
      alerta_msg = (
          "⚠️ ALERTA: A Impressão Digital só funciona em 100% Poliéster (ex: Dry"
          " Fit)!"
      )
    self.label_alerta.configure(text=alerta_msg)

    if total_pecas <= 0:
      self.txt_marcelo.delete("0.0", "end")
      self.txt_marcelo.insert(
          "0.0", "Informe as quantidades na grade de tamanhos."
      )
      self.txt_cliente.delete("0.0", "end")
      self.txt_cliente.insert("0.0", "Informe as quantidades na grade.")
      return

    # 2. Cálculo do Tecido
    if tipo_tec == "piquet_4":
      kg_bruto = total_pecas / 4.0
    elif tipo_tec == "piquet_3":
      kg_bruto = total_pecas / 3.0
    elif tipo_tec == "moletom":
      pmg = sum(d.get(t, 0) for t in ["P", "M", "G"])
      outros = sum(d.get(t, 0) for t in ["PP", "GG", "XG", "XGG"])
      kg_bruto = (pmg * 0.8) + (outros * 1.1)
    else:
      pp_p_m_g = sum(d.get(t, 0) for t in ["PP", "P", "M", "G"])
      gg = d.get("GG", 0)
      xg_xgg = sum(d.get(t, 0) for t in ["XG", "XGG"])
      kg_bruto = (pp_p_m_g / 4.0) + (gg / 3.0) + (xg_xgg / 2.0)

    kg_comprado = math.ceil(kg_bruto * 2) / 2.0
    if kg_comprado < 1.0:
      kg_comprado = 1.0

    custo_tecido_total = kg_comprado * preco_kg

    # 3. Cálculo da Costura + Aviamentos
    modelo_escolhido = self.var_modelo.get()
    if "Polo" in modelo_escolhido:
      custo_unit_costura = 8.00
    elif "Moletom Fechado" in modelo_escolhido:
      custo_unit_costura = 10.00
    elif "Moletom Aberto" in modelo_escolhido:
      custo_unit_costura = 21.00
    else:
      custo_unit_costura = 5.00  # Camiseta padrão

    custo_costura_total = custo_unit_costura * total_pecas

    # 4. Cálculo da Estampa
    custo_estampa_total = 0.0
    detalhes_estampa_str = "Sem estampa"

    if est_escolhida == "Silk Screen":
      try:
        n_cores = int(self.ent_cores_silk.get().strip() or 1)
      except ValueError:
        n_cores = 1
      qtd_cobranca_silk = max(total_pecas, 10)
      custo_por_peca_silk = 1.50 + (n_cores * 0.70)
      custo_estampa_total = custo_por_peca_silk * qtd_cobranca_silk
      detalhes_estampa_str = (
          f"Silk Screen ({n_cores} cor(es)): R$ {custo_por_peca_silk:.2f}/pç"
          f" (Lote mín. cobrado: {qtd_cobranca_silk} pçs)"
      )

    elif est_escolhida == "Digital":
      tipo_dig = self.var_dig_tipo.get()
      if "Frente e Costas" in tipo_dig or "Total" in tipo_dig:
        custo_unit_dig = 25.00
        detalhes_estampa_str = "Impressão Digital Total / Frente e Costas"
      else:
        custo_unit_dig = 8.00
        detalhes_estampa_str = "Impressão Digital Localizada"
      custo_estampa_total = custo_unit_dig * total_pecas

    elif est_escolhida == "DTF":
      try:
        larg = float(self.ent_dtf_larg.get().strip() or 20)
        alt = float(self.ent_dtf_alt.get().strip() or 25)
      except ValueError:
        larg, alt = 20, 25

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

    # 5. Custos Extras / Frete
    try:
      custo_extra = float(self.ent_frete.get().strip() or 0.0)
    except ValueError:
      custo_extra = 0.0

    # 6. Totais Gerais
    custo_geral_total = (
        custo_tecido_total + custo_costura_total + custo_estampa_total + custo_extra
    )
    custo_unitario_final = custo_geral_total / total_pecas

    # 7. Montagem dos Textos de Saída
    grade_str = ", ".join([f"{t}: {v}" for t, v in d.items() if v > 0])
    
    # Texto para o Marcelo
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
    self.txt_marcelo.delete("0.0", "end")
    self.txt_marcelo.insert("0.0", texto_m)

    # Texto para o Cliente
    texto_c = f"""=== ORÇAMENTO COMERCIAL ===
Quantidade: {total_pecas} peça(s)
Item: {modelo_escolhido.split('(')[0].strip()} em {tecido_nome} com {est_escolhida.lower()}

VALOR TOTAL DO PEDIDO: R$ {custo_geral_total:.2f}
VALOR POR UNIDADE: R$ {custo_unitario_final:.2f} cada
"""
    self.txt_cliente.delete("0.0", "end")
    self.txt_cliente.insert("0.0", texto_c)


if __name__ == "__main__":
  app = AppBenelliCompletoFinal()
  app.mainloop()
